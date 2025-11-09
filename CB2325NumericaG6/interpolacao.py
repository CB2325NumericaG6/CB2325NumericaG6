from typing import Callable, Sequence, Optional, List, Tuple
from .core import RealFunction, Interval
from .polinomios import Polinomio
from .raizes import bisseccao

Interpolator = Callable[[float], float]

def hermite_interp(x: Sequence[float], y: Sequence[float], dy: Sequence[float]) -> Interpolator:
    """
    Creates a Hermite polynomial interpolation function from a set of X,Y coordinates
    and their derivatives.

    Args:
        x (Sequence[float]): X-axis coordinates.
        y (Sequence[float]): Y-axis values at the coordinates.
        dy (Sequence[float]): Derivative values at the coordinates.
    
    Returns:
        Interpolator: A callable function that evaluates the Hermite interpolating polynomial.
    
    Raises:
        ValueError: If x, y, dy have different lengths or contain fewer than two points.
    """
    if len(x) != len(y) or len(x) != len(dy) or len(x) < 2:
        raise ValueError(
            f"x, y, dy must have the same length and contain at least two points "
        )
    
    n = len(x)

    def P(X: float) -> float:
        total = 0.0
        for i in range(n):
            # Lagrange polynome L_i(x)
            Li = 1.0
            for j in range(n):
                if j != i:
                    Li *= (X - x[j]) / (x[i] - x[j])
            
            # deff of L_i in x_i
            Li_prime = sum(
                1 / (x[i] - x[m]) for m in range(n) if m != i
            )
            
            # Hermite polynomial base for H_i and K_i
            Hi = (1 - 2*Li_prime*(X - x[i])) * Li**2
            Ki = (X - x[i]) * Li**2
            
            total += y[i]*Hi + dy[i]*Ki
        return total

    return P

def poly_interp(x: Sequence[float], y: Sequence[float]) -> Interpolator:
    """
    Creates a polynomial interpolation function from a set of X and Y coordinates,
    using the Lagrange form.

    Args:
        x (Sequence[float]): Sequence of X-axis coordinates.
        y (Sequence[float]): Sequence of Y-axis coordinates.

    Returns:
        Interpolator: A callable function that evaluates the interpolating polynomial
        for any given float input.

    Raises:
        ValueError: If x and y have different lengths or contain fewer than two points.
    """
    if len(x) != len(y) or len(x) < 2:
        raise ValueError(f"x and y must have the same length ({len(x)} != {len(y)}) and have atleast 2 points.")
    
    n = len(x)

    def P(X: float) -> float:
        total = 0.0
        for i in range(n):
            Li = 1.0
            for j in range(n):
                if i != j:
                    Li *= (X - x[j]) / (x[i] - x[j])
            total += y[i] * Li
        return total

    return P

class PiecewiseLinearFunction(RealFunction):
    def __init__(self, x: Sequence[float], y: Sequence[float], domain: Optional[Interval] = None):
        self.X = x
        self.Y = y
        self.domain = domain if domain else Interval(min(x), max(x))
        self.f = self.evaluate # O Callable principal para RealFunction

    def makePolynomialSegment(self, x1, x2, y1, y2) -> Polinomio:
        if x1 == x2:
            raise ValueError("Pontos x1 e x2 são o mesmo. Não é possível criar um segmento.")

        slope = (y2-y1)/(x2-x1)
        c0 = y1 - slope * x1
        segmentDomain = Interval(min(x1, x2), max(x1, x2))

        pol = Polinomio([slope, c0], segmentDomain) 

        return pol

    @property
    def prime(self) -> Callable[[float], float]: #type: ignore
        """
        Retorna a função que calcula a derivada (inclinação constante) 
        da interpolação linear por partes. A derivada é indefinida nos pontos de referência.
        """
        
        # O self.prime da RealFunction é um Callable. Retornamos uma função que implementa a lógica da derivada.
        def piecewisePrimeFunction(v: float) -> float:
            if not (self.X[0] <= v <= self.X[-1]):
                raise ValueError(f"O ponto {v} está fora do domínio de interpolação.")
            
            n = len(self.X)
            
            for x_i in self.X:
                if abs(v - x_i) < 1e-12: 
                    raise ValueError(f"A derivada é descontínua e indefinida no nó x={v}.")

            start, end = 0, n - 1

            while end - start != 1:
                mid = (end + start) // 2
                if self.X[mid] > v:
                    end = mid
                else:
                    start = mid
            
            x1, x2 = self.X[start], self.X[end]
            y1, y2 = self.Y[start], self.Y[end]
            
            slope = (y2 - y1) / (x2 - x1)
            
            return slope

        return piecewisePrimeFunction

    def evaluate(self, v: float) -> float:
        n = len(self.X)
        if v > self.X[-1]:
            start, end = n - 2, n - 1
        elif v < self.X[0]:
            start, end = 0, 1
        elif v == self.X[0]:
            return self.Y[0]
        elif v == self.X[-1]:
            return self.Y[-1]
        else:
            start, end = 0, n - 1 
            while end - start != 1:
                mid = (end + start) // 2
                if self.X[mid] > v:
                    end = mid
                elif self.X[mid] < v:
                    start = mid
                else:
                    return self.Y[mid] 

        x1, x2 = self.X[start], self.X[end]
        y1, y2 = self.Y[start], self.Y[end]

        return y1 + (v - x1) * ((y2 - y1) / (x2 - x1))
    
    def find_root_segments(self) -> List[Tuple[float, float]]:
        """
        Retorna uma lista de intervalos [a, b] onde f(a) * f(b) < 0.
        """

        segments = []
        for i in range(len(self.X) - 1):
            y_i = self.Y[i]
            y_i_plus_1 = self.Y[i+1]
            
            # Se os sinais são opostos (garantia da raiz)
            if y_i * y_i_plus_1 < 0:
                segments.append((self.X[i], self.X[i+1]))
                
            if y_i == 0:
                segments.append((self.X[i], self.X[i]))

        if self.Y[-1] == 0:
            segments.append((self.X[-1], self.X[-1]))
            
        return segments
    
def linear_interp(x: Sequence, y: Sequence) -> PiecewiseLinearFunction:
    """Cria uma função de interpolação (e extrapolação)s linear a partir de um par de sequências de coordenadas X,Y
    assumindo que os valores X são estritamente crescentes.

    Args:
        x (Sequence): Lista de coordenadas do eixo X (estritamente crescente)
        y (Sequence): Lista de coordenadas do eixo Y
    
    Returns:
        Interpolator: Uma função que retorna o valor interpolado linearmente baseado nos valores X, Y.
    Raises:
        ValueError: Se a quantidade de elementos de X e Y forem diferentes ou tiverem menos de dois pontos.
    Examples:
        >>> x = [0, 2, 4, 5]
        >>> y = [1, 2, 0, 4]
        >>> p = linear_interp(x, y)
        >>> print(p(1.5))
        1.75
    """
    
    if len(x) != len(y):
        raise ValueError("Lenght of X is different of Y")
    if len(x) < 2:
        raise ValueError("There must be atleast 2 points")
    
    return PiecewiseLinearFunction(x, y)