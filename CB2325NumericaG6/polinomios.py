from typing import List, Tuple

class Polinomio:
    """
    Representa um polinômio como uma lista de coeficientes, ordenados 
    do termo de **maior grau** para o termo constante.

    P[0] é o coeficiente do maior grau, e o grau é dado por len(P) - 1.
    Exemplo: O polinômio P(x) = 3x^2 + 2x - 1 é representado por [3.0, 2.0, -1.0].
    """

    def __init__(self, values: List[float]):
        self._values = values
        if float(values[0]) == 0.0:
            self._clearZeros()
    
    def __repr__(self):
        return str(self._values)
    
    def __len__(self):
        return len(self._values)
    
    def __getitem__(self, index):
        size = len(self._values)
        if abs(index) >= size:
            raise IndexError("index out of range")
        elif index < 0:
            return self._values[size + index]
        else:
            return self._values[index]

    def __setitem__(self, index, value):
        size = len(self._values)
        if abs(index) >= size:
            raise IndexError("assignment index out of range")
        elif index < 0:
            self._values[size + index] = value
        else:
            self._values[index] = value

    def _clearZeros(self):
        """
        Função interna para remover os 0s dos líderes
        """
        count = 0
        for coef in self._values:
            if coef == 0.0:
                count += 1
            else:
                break
        
        if count == len(self._values):
            self._values = []
        elif count> 0:
            self._values = self._values[count:]
        
        if not self._values:
            self._values.append(0.0)

    
    def _clean_by_tolerance(self, tolerance: float) -> 'Polinomio':
        """
        TODO: Talvez substituir quando o calculo de erros for implementado em .erros.py

        Cria um novo Polinomio zerando coeficientes abaixo da tolerância para evitar erros numéricos.
        """
        new_values = [
            coef if abs(coef) >= tolerance else 0.0
            for coef in self._values
        ]
        return Polinomio(new_values)

    @property
    def degree(self) -> int:
        return len(self._values)-1
    
    def evaluate(self, x: float) -> float:
        """
            Avalia o polinômio P(x) para um dado valor de x usando o Método de Horner.
            
            P é uma lista de coeficientes em ordem decrescente: [c_n, ..., c_0].
            
            Args:
                x (float): O ponto onde o polinômio será avaliado.
                
            Returns:
                float: O valor P(x).
            
            Examples:
                >>> P = Polinomio([2,3,4])
                >>> val = P.evaluate(1)
                >>> print(val)
                9

        """
        if not self._values:
            return 0.0

        resultado = self._values[0] 
        
        for i in range(1, len(self._values)):
            resultado = resultado * x + self._values[i]
            
        return resultado
    
    def __mul__(self, other: float | int) -> 'Polinomio':
        if isinstance(other, (float, int)):
            newValues = [c * float(other) for c in self._values]
            return Polinomio(newValues)
        return NotImplemented

    def __rmul__(self, other: float | int) -> 'Polinomio':
        return self.__mul__(other)
    
    def __neg__(self) -> 'Polinomio':
        new_values = [-c for c in self._values]
        return Polinomio(new_values)
    
    def __add__(self, other: 'Polinomio') -> 'Polinomio':
        p1Values = self._values
        p2Values = other._values
        
        maxLen = max(len(p1Values), len(p2Values))

        p1Reversed = p1Values[::-1]
        p2Reversed = p2Values[::-1]
        
        sumReverse = []
        for i in range(maxLen):
            c1 = p1Reversed[i] if i < len(p1Reversed) else 0.0
            c2 = p2Reversed[i] if i < len(p2Reversed) else 0.0
            sumReverse.append(c1 + c2)
            
        return Polinomio(sumReverse[::-1])
    
    def __sub__(self, other: 'Polinomio') -> 'Polinomio':
        negOther = -other 
        return self + negOther
    
    def __eq__(self):
        return NotImplemented

    def divideBy(self, divisor: 'Polinomio', tolerance: float = 1e-12) -> Tuple['Polinomio', 'Polinomio']:
        """
            Realiza a divisão polinomial A / B (self / divisor) e retorna (Quociente, remainder).

            Args:
                divisor (Polinomio): Polinomio divisor
                tolerance (float, optional): Tolerância para checagem de zero, usado para
                    tratar erros de ponto flutuante. O valor padrão é 1e-12.

            Returns:
                Polinomio: Polinomio derivado

            Examples:
                >>> p1 = Polinomio([4,6,8])
                >>> p2 = Polinomio([2,3,4])
                >>> print(p1.divideBy(p2))
                ([2.0], [0.0])
        """

        if divisor.degree < 0 or abs(divisor._values[0]) < tolerance:
            raise ValueError("Cannot divide by the zero polynomial.")

        if self.degree < divisor.degree:
            return Polinomio([0.0]), Polinomio(self._values)

        mainDivisor = divisor._values[0]
        divisorDegree = divisor.degree
        
        quotientCoeffs = [0.0] * (self.degree - divisorDegree + 1)

        remainder = Polinomio(self._values) 
        
        while remainder.degree >= divisorDegree:
            mainRemainder = remainder._values[0]
            
            degreeDifference = remainder.degree - divisorDegree
            
            qCoeff = mainRemainder / mainDivisor

            qIdx = self.degree - remainder.degree
            quotientCoeffs[qIdx] = qCoeff
    
            multipliedTherm = divisor * qCoeff 

            shiftCoeffs = multipliedTherm._values + [0.0] * degreeDifference
            thermToSub = Polinomio(shiftCoeffs)

            remainder = remainder - thermToSub 
            remainder = remainder._clean_by_tolerance(tolerance)

        if remainder.degree < 0:
            remainder = Polinomio([0.0])

        return Polinomio(quotientCoeffs), remainder
    
def diffPol(pol: Polinomio) -> Polinomio:
    """
        Retorna a derivada de um polinomio.

        Args:
            pol (Polinomio): Polinomio a ser derivado.

        Returns:
            Polinomio: Polinomio derivado

        Examples:
            >>> pol = Polinomio([-3.0,2.0,4.0])
            >>> dPol = diffPol(pol)
            >>> print(dPol)
            [-6.0,2.0]
    """

    if len(pol) <= 1:
        return Polinomio([0])
    
    derivative = []

    for i in range(pol.degree):
        derivative.append(pol[i]*(pol.degree-i))

    return Polinomio(derivative)

if __name__ == "__main__":
    pol = Polinomio([2,5,4,8,5,-3.0,2.0,4.0])
    p1 = Polinomio([4,6,8])
    p2 = Polinomio([2,3,4])

    p3 = p1.divideBy(p2, tolerance=1e-5)

    print(p2*2 - p1)
    print(p3)

    dPol = diffPol(pol)
    print(dPol)

    print(p2.evaluate(1))