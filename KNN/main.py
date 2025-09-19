
import cmath
import matplotlib
from matplotlib import pyplot as plt


def CalcularMatriz(x, y):
    matriz = []
    for j in range(len(x)):
        distacia = []
        for i in range(len(x)):
            d = ((x[j] - x[i])**2 + (y[j]-y[i])**2)**0.5
            d = round(d, 2)
            distacia.append(d)
        matriz.append(d)
    return matriz


x = [5, 8, 4, 10, 3]
y = [7, 11, 3, 9, 2]
matriz = CalcularMatriz(x,y)
for linha in matriz:
    print(linha)

plt.plot(x,y, "bo")
plt.show()





