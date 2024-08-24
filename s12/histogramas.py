import numpy as np
import matplotlib.pyplot as plt

# Generación de números aleatorios:
# Todas se encuentran dentro un submódulo:
""" from np.random import * """
# Aunque no sea muy común, se puede hacer así.

np.random.rand() # Genera números aleatorios de 0 a 1 pero no los hace de forma "distribución normal"
np.random.randn() # Genera números aleatorios con media en 0 y desvest en 1 (estos sí son dist. normales y estándar)

data = np.random.normal(
    loc=  0, # El valor correspondiente a la media
    scale= 1, # El valor correspondiente a la desviación std
    size= 10000,  # El número de datos que deseamos generar
)

# Los datos se van a guardar en la variable "data"

# Generación de histogramas

# Esto se hace en matplotlib.pyplot con el método hist()
plt.hist()