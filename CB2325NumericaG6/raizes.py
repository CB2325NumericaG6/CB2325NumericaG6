from typing import Literal, Callable


def secante(f: Callable, a: float, b: float, tol: float) -> float:
    """
    Método da secante:
        Consiste em pegar dois pontos próximos a e b e então realiza a apro-
        ximação da raiz a partir do ponto onde a reta que intercepta ambos os
        pontos encontra o eixo X (m), repetindo o processo até que abs(f(m)) 
        seja menor que a tolerância exigida.

    Parametros:
        f: Função a ser analizada
        a: Ponto inicial da função f
        b: Ponto final da função f
        tol: Tolerância para o erro da aproximação final

    Saida:
        Aproximação da raiz da função encontrada.
    """

    a, b = (a, b) if a < b else (b, a)

    aproximacao = (f(b) * a - f(a) * b) / (f(b) - f(a))
    while abs(f(aproximacao)) >  tol:
        a = b
        b = aproximacao
        aproximacao = (f(b) * a - f(a) * b) / (f(b) - f(a))
    return aproximacao


    
def bissecao(f: Callable, a: float, b: float, tol: float) -> float:
    """
    Método da bisseção:
        Consiste em pegar um intervalo a e b na qual f(a) tem sinal oposto a f(b),
        então realiza a aproximação da raiz a partir de média do intervalo (m), 
        repetindo o processo até que abs(f(m)) seja menor que a tolerância exigida.

    Parametros:
        f: Função a ser analizada
        a: Intervalo inicial da função f
        b: Intervalo final da função f
        tol: Tolerancia para o erro da aproximação final

    Saida:
        Aproximação da raiz da função no intervalo [a, b]
    """

    if f(a) * f(b) > 0:
        raise ValueError('f(a) tem o mesmo sinal que f(b), não há garantia da existencia de uma raiz')
    
    a, b = (a, b) if f(a) < f(b) else (b, a)

    aproximacao = (a + b) / 2
    while abs(f(aproximacao)) > tol:
        if f(aproximacao) > 0:
            b = aproximacao
        else:
            a = aproximacao
        
        aproximacao = (a + b) / 2

    return aproximacao

def newton_raphson(f: Callable, df: Callable, a:float, tol: float) -> float:
    """
    Método de Newton Raphson:
        Consiste em pegar um ponto a e então realiza a aproximação da raiz a
        partir do ponto onde a reta tangente o ponto a encontra o eixo X (m),
        repetindo o processo até que abs(f(m)) seja menor que a tolerância 
        exigida.

    Parametros:
        f: Função a ser analizada
        df: Derivada de f
        a: Ponto inicial da função f
        tol: Tolerancia para o erro da aproximação final

    Saida:
        Aproximação da raiz da função encontrada.
    """

    aproximacao = a - f(a)/df(a)
    while abs(f(aproximacao)) > tol:
        a = aproximacao
        aproximacao = a - f(a)/df(a)
    
    return aproximacao


if __name__ == '__main__':
    f = lambda x: x**2 - 16
    df = lambda x: 2 * x

    print(bissecao(f, 3, 5, 10 **-6))
    print(secante(f, 3, 5, 10 **-6))
    print(newton_raphson(f, df, 5, 10 **-6))
