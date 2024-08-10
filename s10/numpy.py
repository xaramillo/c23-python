# Importación básica de numpy
#import numpy
#numpy.array([[1, 2, 3], [4, 5, 6]])

# Forma más común para trabajar con numpy con su alias "np"
import numpy as np
#np.array([[1, 2, 3], [4, 5, 6]])

# Para temas de optimización, solo se carga la función requerida
#from numpy import array
#array([[1, 2, 3], [4, 5, 6]])

# Para agregar un alias se pone la cláusula "as"
#from numpy import array as arreglo
#arreglo([[1, 2, 3], [4, 5, 6]])


# Creación de arrays dentro de numpy:

lista_num = [14,2004,15,1100,227]
print('Propiedades de la lista')
print(' Objeto:', type(lista_num))
print( 'Tamaño:'  , len(lista_num))
print( 'Tipo:', [type(t) for t in lista_num])
#
arr = np.array( lista_num )
print('Propiedades del array')
print(' Objeto:', type(arr))
print( 'Tamaño:'  , arr.size )
print( 'Tipo:', arr.dtype)

# Métodos de selección

# Crear array 3x3
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Extraer la primera fila
first_row = arr[0, :]

# Extraer la última columna
last_column = arr[:, -1]

# Extraer subarray central 2x2
subarray = arr[1:, 1:]