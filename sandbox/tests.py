import sys, os
sys.path.append(os.path.abspath(os.path.join(os.getcwd(), '..')))

from CB2325NumericaG6 import core, integracao, interpolacao, polinomios, aproximacao
import matplotlib.pyplot as plt

x = [0.0,1.0,2.0,3.0,4.0]
y = [2.0,1,2,0,0]
dy = [-1,2,5,-1,0]

a = aproximacao.ajuste_linear(x,y)
b = aproximacao.ajuste_polinomial(x,y, 3)

# Criamos um dicionário {"Nome": Polinomio"}
funcaoA = {"Linear": a}
funcaoB = {"Linear": b}

intervalo = core.Interval(0,4)

aproximacao.plot_ajuste(x,y, funcaoA , intervalo)

aproximacao.plot_ajuste(x,y, funcaoB, intervalo)

funcaoC = interpolacao.poly_interp(x,y)
funcaoC.plot(domain=intervalo)

funcaoD = interpolacao.linear_interp(x,y)
funcaoD.plot()

funcaoE = interpolacao.hermite_interp(x, y, dy)
funcaoE.plot(domain=intervalo)

plt.show()
