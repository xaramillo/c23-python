# Ejercicio de la semana 07
mi_lista = [67,23,6,9,15,13] # mi_lista es el iterable
tamano_de_lista = len(mi_lista)
intervalo = range(0,tamano_de_lista)
for index in intervalo: # index es nuestro apuntador, intervalo es el iterable auxiliar útil
    mi_lista[index] = mi_lista[index] + 10 # Toda esta línea representa la Expresión
#print(mi_lista)

"""
for n in mi_lista: # n era el apuntador, mi_lista era el iterable
    print("Cada elemento de la lista es: ")
    mi_lista[n] = n + 10 # Toda esta línea representa la Expresión
    print(n)
"""

# El mismo ejercicio en la semana 08

# iterable: mi_lista
# elemento: n
# expresion: n + 10

# [expresion for elemento in iterable]
comprehension = [ n + 10 for n in mi_lista]
print(comprehension)