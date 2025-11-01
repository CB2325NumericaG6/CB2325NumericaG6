from typing import Callable, Sequence

Interpolator = Callable[[float], float]

def poly_interp(x, y) -> float:
    # TODO: Implement this
    raise NotImplementedError

def linear_interp(x: Sequence, y: Sequence) -> Interpolator:
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

    if len(x) != len(y) or len(x) < 2:
        raise ValueError(f"X e Y precisam ter o mesmo tamanho: ({len(x)} != {len(y)}) e também ter no mínimo dois pontos")
    
    def interpolation(v) -> float:
        start,end = 0, len(x)

        if v > x[-1]:
            start,end = len(x)-2, len(x)-1
        elif v < x[0]:
            start,end = (0,1)
        else:
            #Performs binary search to find the bounding points of v
            while end-start != 1:
                mid = (end+start)//2
                if x[mid] > v:
                    end = mid
                elif x[mid] < v:
                    start = mid
                else:
                    #Returns point if it is defined in X-axis set
                    return y[mid]
                
        x1,x2 = x[start],x[end]
        y1,y2 = y[start],y[end]
        
        return y1 + (v-x1)*((y2-y1)/(x2-x1))

    return interpolation