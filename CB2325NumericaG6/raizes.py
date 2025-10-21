from typing import Literal, Callable

def raiz(f: Callable, a, b, tol: float, method: Literal["secante", "bissecao", "newton-raphson"]) -> float:
    def secante(f: Callable, a, b, tol: float) -> float:
        raise NotImplementedError()
    
    def bissecao(f: Callable, a, b, tol: float) -> float:
        """
        Metodo da bisseção:
            Consiste em pegar um intervalo a e b na qual f(a) tem sinal oposto a f(b),
            então realiza a aproximação da raiz a partir de média do intervalo, repe-
            tindo o processo até que f(média) seja menor que a tolerancia exigida

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

        media = (a + b) / 2
        while abs(f(media)) > tol:
            if f(media) > 0:
                b = media
            else:
                a = media
            
            media = (a + b) / 2

        return media
    
    def newton_raphson(f: Callable, a, b, tol: float):
        raise NotImplementedError()
    
    methods = {
        'secante': secante,
        'bissecao': bissecao,
        'newton-raphson': newton_raphson
    }

    return methods[method](f, a, b, tol)

print(raiz(lambda x: x**2 - 10, -5, 2, 10 **-6, 'bissecao'))
