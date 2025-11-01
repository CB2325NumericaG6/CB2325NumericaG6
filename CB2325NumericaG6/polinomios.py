from typing import List

class Polinomio:
    """
    Representa um polinômio como uma lista de coeficientes, ordenados 
    do termo de **maior grau** para o termo constante.

    P[0] é o coeficiente do maior grau, e o grau é dado por len(P) - 1.
    Exemplo: O polinômio P(x) = 3x^2 + 2x - 1 é representado por [3.0, 2.0, -1.0].
    """

    def __init__(self, values: List[float]):
        self._values = values
        self._clearZeros()
    
    def __repr__(self):
        return str(self._values)
    
    def __len__(self):
        return len(self._values)
    
    def __getitem__(self, index):
        size = len(self._values)
        if abs(index) >= size:
            raise IndexError("index out of range")
        elif index < 0:
            return self._values[size + index]
        else:
            return self._values[index]

    def __setitem__(self, index, value):
        size = len(self._values)
        if abs(index) >= size:
            raise IndexError("assignment index out of range")
        elif index < 0:
            self._values[size + index] = value
        else:
            self._values[index] = value

    def _clearZeros(self):
        """
        Função interna para remover os 0s dos líderes
        """
        count = 0
        for coef in self._values:
            if coef == 0.0:
                count += 1
            else:
                break
        
        if count < len(self._values) - 1:
            self._values = self._values[count:]
        
        if not self._values:
            self._values.append(0.0)

    @property
    def degree(self) -> int:
        return len(self._values)-1
    
def diffPol(pol: Polinomio) -> Polinomio:
    """
        Retorna a derivada de um polinomio.

        Args:
            pol (Polinomio): Polinomio a ser derivado.

        Returns:
            Polinomio: Polinomio derivado

        Examples:
            >>> pol = Polinomio([-3.0,2.0,4.0])
            >>> dPol = diffPol(pol)
            >>> print(dPol)
            [-6.0,2.0]
    """

    if len(pol) <= 1:
        return Polinomio([0])
    
    derivative = []

    for i in range(pol.degree):
        derivative.append(pol[i]*(pol.degree-i))

    return Polinomio(derivative)

if __name__ == "__main__":
    pol = Polinomio([-3.0,2.0,4.0])
    dPol = diffPol(pol)
    print(dPol)