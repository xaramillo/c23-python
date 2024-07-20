# Colecciones

# Métodos sencillos para listas

mi_lista_vacia = []
mi_lista = [67,23,6,9]

mi_lista.append(15)

mi_lista = mi_lista + [13]

print(" Ejemplo de definiciones de lista:")
print(mi_lista)
tamano_de_lista = len(mi_lista)
print("Tamaño de la lista: ",tamano_de_lista )

# queremos sumar un 10 a todos los elementos de mi_lista:

"""
for n in mi_lista:
    print("Cada elemento de la lista es: ")
    mi_lista[n] = n + 10
    print(n)
"""
print("Ejercicio para sumar elementos a una lista")

print("para acceder a elementos de una lista por índice debemos definir un rango")
print("Rango de números:")

intervalo = range(0,tamano_de_lista)

print(list(intervalo))

print("Inicio del ciclo: ")
for index in intervalo:
    print( "\tvalor del índice",index, )    
    print(f"\tsumar 10 + {mi_lista[index]} a nuestra lista")
    mi_lista[index] = mi_lista[index] + 10

print("Resultado: ")
print(mi_lista)

# Métodos sencillos para tuplas

print("Cómo consultar elementos de una tupla:")
coordenadas = (1000.0,500.0)

print(f"coords (X:Y) {coordenadas}")
print("coords (X:Y)", coordenadas)
print("coords (X:Y) {coordenadas}")

coordenadas_x_modificada = coordenadas[0]+1
print(f" coord X: {coordenadas_x_modificada} ")

# Métodos sencillos para conjuntos

print("ejercicio de conjuntos")

set_a = {1,2,3,4,7}
set_b = {1,2,4,5,6}

union = set_a | set_b
print("Conjunto union set_a | set_b :")
print(union)

print(f"Intersección: { set_a & set_b } ")
print(f"Diferencia: { set_a - set_b } ")

lista_repetida = [1,1,1,1,1,1,2,2,2,3,3]
print(f"Elementos de lista repetida: {lista_repetida}")
print(f"Conjunto de elementos únicos: {set(lista_repetida)}")

# Diccionarios

dcc = {"llave1" : 'cadena de texto',
       "llave2" : set(lista_repetida),
       3: "solamente es un numero",
       }

print(dcc[3])


# Ejemplo para un programador de Java

"""
Crear una clase <nombre_de clase>:
    clase.atributo1 
    clase.atributo2

"""

nombre = {
    'atributo1' : 'Juan',
    'atributo2' : 3
}