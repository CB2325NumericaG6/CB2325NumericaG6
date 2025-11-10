import math
import statistics
from polinomios import Polinomio
def ajuste_linear(x: list[float], y: list[float]) -> Polinomio:
    """
    Ajusta y = a*x + b aos pontos (x, y) por mínimos quadrados (erro vertical).

    Args:
        x: Valores da variável independente.
        y: Valores da variável dependente (mesmo tamanho de x).

    Returns:
        (a, b): Inclinação e intercepto da reta ajustada.

    Raises:
        ValueError: Tamanhos diferentes ou menos de dois pontos.
        ZeroDivisionError: Variância de x igual a zero.
    """
    if len(x) != len(y):
        raise ValueError("Ambas as listas devem ter o mesmo tamanho.")
    n = len(x)
    if n < 2:
        raise ValueError("Precisa de pelo menos dois pontos.")

    mx = statistics.mean(x)
    my = statistics.mean(y)

    cov_xy = math.fsum((xi - mx) * (yi - my) for xi, yi in zip(x, y))
    var_x  = math.fsum((xi - mx) ** 2 for xi in x)

    if var_x == 0.0:
        raise ZeroDivisionError("A variância de x é zero.")

    a = cov_xy / var_x
    b = my - a * mx
    return Polinomio([a,b])


if __name__ == "__main__":
    x = [0, 1, 2, 3, 4]
    y = [1.1, 1.9, 3.0, 3.9, 5.2]
    a, b = ajuste_linear(x, y)
    print(f"y = {a:.2f}x + {b:.2f}")
