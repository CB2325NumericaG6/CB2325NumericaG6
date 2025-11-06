import numpy as np

def erro_absoluto(valor_real, valor_aprox):
    """
    Calcula o erro absoluto entre um ou mais valores reais e aproximados.
    
    Esta função é 'vectorizada': ela aceita tanto números únicos
    quanto arrays NumPy.

    Fórmula: ea = |valor_real - valor_aprox|
    
    Args:
        valor_real (float ou np.ndarray): O valor exato ou de referência.
        valor_aprox (float ou np.ndarray): O valor obtido ou medido.

    Returns:
        float ou np.ndarray: O erro absoluto.
    """
    # np.abs lida automaticamente com escalares e arrays
    return np.abs(valor_real - valor_aprox)
