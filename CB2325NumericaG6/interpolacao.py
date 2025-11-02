from typing import Callable, Sequence

Interpolator = Callable[[float], float]

def Hermite_poly_interp(x, y) -> float:
    #Teste commit
    print("Teste")
    # TODO: Implement this
    raise NotImplementedError

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


def linear_interp(x: Sequence, y: Sequence) -> Interpolator:
    """Creates a linear interpolation function from a set of X,Y coordinates, 
    assuming a strictly increasing set of X-values.

    Args:
        x (Sequence): X-axis coordinate list
        y (Sequence): Y-axis coordinate list
    
    Returns:
        Callable([float], float): Callable returns linearly-interpolated value based on given sets
          for a certain point.
    """

    if len(x) != len(y) or len(x) < 2:
        raise ValueError(f"x and y must have the same length ({len(x)} != {len(y)}) and have atleast 2 points.")
    
    def interpolation(v) -> float:
        start,end = 0, len(x)

        if v > x[-1]:
            start,end = len(x)-2, len(x)-1
        elif v < x[0]:
            start,end = (0,1)
        else:
            #Performs binary search to 
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