def poly_interp(x, y) -> float:
    # TODO: Implement this
    raise NotImplementedError

def linear_interp(x: list, y: list) -> callable:
    """Creates a linear interpolation function from a set of X,Y coordinates,
    assuming a strictly increasing set of X-values.

    Args:
        x: X-axis coordinate list
        y: Y-axis coordinate list
    
    Returns:
        callable: Return linear-interpolated value for a certain point.
    """

    if len(x) != len(y) or len(x) < 2:
        raise ValueError("x and y mus have the same length and have atleast 2 points.")
    
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