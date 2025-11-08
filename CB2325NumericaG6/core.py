from typing import Callable, Optional
import matplotlib.pyplot as plt

# Gostei muito da implementação dessas classes da lista 7 do professor então decidi implementar com pequenas modificações
class Domain:
    """
    Define o domínio no qual uma função real existe.
    """
    min = None
    max = None

    def __contains__(self, x):
        raise NotImplementedError
    
    def __repr__(self):
        raise NotImplementedError

    def __str__(self):
        return self.__repr__()
    
    def copy(self):
        raise NotImplementedError 


class Interval(Domain):
    """
    Define um intervalo de números reais.
    """
    def __init__(self, p1, p2):
        self.inff, self.supp = min(p1, p2), max(p1, p2)
    
    @property
    def min(self):
        return self.inff

    @property
    def max(self):
        return self.supp
    
    @property
    def size(self):
        return (self.max - self.min)
    
    @property
    def haf(self):
        return (self.max + self.min)/2.0
    
    def __contains__(self, x):
        return NotImplementedError

    def __str__(self):
        return f'[{self.inff:2.4f}, {self.supp:2.4f}]' 

    def __repr__(self):
        return f'[{self.inff!r:2.4f}, {self.supp!r:2.4f}]'
    
    def copy(self):
        return Interval(self.inff, self.supp)


class RealFunction:
    """
    Classe abstrata que deve ser utilizada para implementação de funções reais, e.g. Polinomios
    """

    f: Callable[[float], float]
    prime: Optional[Callable[[float], float]]
    domain: Optional[Domain]
    
    def eval_safe(self, x):
        if self.domain is None or x in self.domain:
            return self.f(x)
        else:
            raise Exception("The number is out of the domain")

    def prime_safe(self, x):
        if self.prime is None:
            raise NotImplementedError("Derivative function (prime) is not defined for this function.")
        if self.domain is None or x in self.domain:
            return self.prime(x)
        else:
            raise Exception("The number is out of the domain")
        
    def __call__(self, x) -> float:
        return self.eval_safe(x)
    
    def plot(self):
        return NotImplementedError
    
def linspace(min: float, max: float, points: int) -> list[float]:
    """
    Retorna uma lista de pontos igualmente distribuídos em um intervalo

    Args:
        min (float): Valor mínimo do intervalo de pontos
        max (float): Vamor máximo do intervalo de pontos
        points (int): Quantidade de pontos

    Returns:
        list[float]: Lista de pontos igualmente distribuídos no intervalo

    Examples:
        >>> valores = linspace(0, 5, 6)
        >>> print(valores)
        [0.0, 1.0, 2.0, 3.0, 4.0, 5.0]
    """
    if points < 2:
        return [min]
    step = (max - min) / (points - 1)
    return [(step * i + min) for i in range(points)]