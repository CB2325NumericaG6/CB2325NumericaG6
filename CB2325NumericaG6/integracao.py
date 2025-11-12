import matplotlib.pyplot as plt
import numpy as np
from typing import Callable


def integral(f:Callable, start: float, end: float, divisions: int) -> float:
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

def plot_integral(f: Callable, start: float, end: float, divisions: int) -> tuple[plt.Figure, plt.Axes]:
    valor_integral = integral(f, start, end, divisions)
    
    fig, ax = plt.subplots()
    
    # Função
    x = np.linspace(start, end, 1000)
    y = f(x)
    ax.plot(x, y, 'b-')
    
    # Trapézios
    x_div = np.linspace(start, end, divisions + 1)
    y_div = f(x_div)
    
    for i in range(divisions):
        ax.fill([x_div[i], x_div[i], x_div[i+1], x_div[i+1]], 
                [0, y_div[i], y_div[i+1], 0], 
                'orange', alpha=0.4)
    
    ax.plot(x_div, y_div, 'ro', markersize=3)
    ax.set_title(f"Integral: {valor_integral:.6f}")
    ax.grid(True)
    
    return fig, ax