import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

#funcao que sera fitada (parametros a,b e c a determinar)
def func(x, a, b, c):
    return a * np.exp(-b * x) + c

#x= 50 pontos entre 0 e 4
xdata = np.linspace(0, 4, 50)


#no caso do seu lab substitua por um vetor com os seus valores. Ex:
#xdata=[0,1,2,3,4]
#voce pode criar um vetor com ydata:
#ydata=[-0.1,0.9,4.05,9.2,16.1]


#No meu exemplo, vou gerar um vetor com um certo ruido para usar de exemplo. Observe:
y = func(xdata, 2.5, 1.3, 0.5)   #gerei aqui os valores puros da funcao em ydata
np.random.seed(1729) #gerando semente de numeros aleatorios
y_noise = 0.2 * np.random.normal(size=xdata.size) #ruido
ydata = y + y_noise  #sinal com ruido


#vou fitar a curva agora
popt, pcov = curve_fit(func, xdata, ydata)

#vou plotar agora os resultados.
plt.plot(xdata, ydata, 'b-', label='data') #valor bruto
plt.plot(xdata, func(xdata, *popt), 'r-', label='fit: a=%5.3f, b=%5.3f, c=%5.3f' % tuple(popt)) #curva ajustada

#configuracoes do grafico
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()