from typing import Callable
from numpy import linspace
# Falta implementar o linspace de core.py

def integral_trapezio(f:Callable, start: float, end: float, divisions: int) -> float:
    """Esse método calcula a integral de uma função por aproximação trapezoidal
    Args:
        f (Callable): Função a ser integrada
        start (float): Ponto inicial do intervalo
        end (float): Ponto final do intervalo
        divisions (int): Número de subdivisões do intervalo: números maiores implicam uma aproximação mais precisa, mas também consome mais CPU.
    Returns:
        float: Valor da integral.
    Examples:
        >>> import math
        >>> f = lambda x: math.sin(x)**2+math.cos(x)**2
        >>> i = integracao.integral(f, 0, 2, 1000)
        >>> print(i)
        2.0
    """
    
    sumVal: float = 0
    Xincrement: float = abs(start-end)/divisions
    
    i: float = start
    while i < end:
        area: float = ( f(i) + f(min(end, i+Xincrement)) )
        area *= Xincrement/2.0 if i+Xincrement < end else (end-i)/2.0
        
        sumVal += area
        i += Xincrement
    
    return sumVal

def integral_riemann(f:Callable, start:float, end:float, divisions:int) -> float:
    """Este método calcula a integral de uma função por
    soma de Riemann
    Args:
        f (Callable): Função a ser integrada
        start (float): Ponto inicial do intervalo
        end (float): Ponto final do intervalo
        divisions (int): Número de subdivisões do intervalo: números maiores implicam uma aproximação mais precisa, mas também consome mais CPU.
    Returns:
        float: Valor da integral.
    Examples:
        >>> f = lambda x: x**2
        >>> i = integracao.integral_riemann(f, 0, 3, 1000)
        >>> print(round(i,2))
        9.0
    """
    base = abs(end - start)/divisions
    retangulos = [base * f(x) for x in linspace(start+base/2,end-base/2, divisions)]
    i = sum(retangulos)

    return i