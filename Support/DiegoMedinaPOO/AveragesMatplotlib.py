# Matplotlib. (4 partes a evaluar)
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats as st

# a) Haga un programa en python en el que registre en un arreglo de numpy el promedio global de cada uno de los
# semestres que ha cursado en la carrera. Si considera que son pocos, puede generarlos con random, pero debe haber
# 10 valores.
averages = []

for i in range(10):
    averages.append(np.random.randint(6, 10))
print(averages)

# b) Muestre en la consola (negra) los valores de: mínimo, máximo, media, mediana y moda.
print("Min:", np.min(averages))
print("Max:", np.max(averages))
print("Mean:", np.mean(averages))
print("Median:", np.median(averages))
mode = st.mode(averages)[0][0]
print("Mode:", mode)


# c) Grafique, con scatter, los valores obtenidos.
plt.scatter(0, np.min(averages), color='red')
plt.scatter(1, np.max(averages), color='green')
plt.scatter(2, np.mean(averages), color='blue')
plt.scatter(3, np.median(averages), color='yellow')
plt.scatter(4, mode, color='black')
plt.show()

# d) Cambie los colores de los puntos.
plt.scatter(0, np.min(averages), color='green')
plt.scatter(1, np.max(averages), color='blue')
plt.scatter(2, np.mean(averages), color='red')
plt.scatter(3, np.median(averages), color='black')
plt.scatter(4, mode, color='yellow')
plt.show()
