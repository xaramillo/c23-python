import matplotlib.pyplot as plt
import numpy as np

data = np.random.randn(1000)

x = np.random.rand(100)
y = x + np.random.randn(100) * 0.1


plt.hist(data, bins=30, alpha=0.7, color='blue')
plt.title('Histograma de Datos Generados')
plt.xlabel('Valor')
plt.ylabel('Frecuencia')
plt.show()