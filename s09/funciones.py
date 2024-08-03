# Funciones

"""
def nombre_de_la_funcion(parámetros):
	'''Documentación opcional de la función'''
	instrucciones
	return valor_de_retorno
"""

def saludo():
    print('Hola')

def saludo_doc():
    """Imprime un saludo"""
    print('Hola')

def saludo_param(nombre):
    """Imprime un saludo"""
    print('Hola' , nombre)

def saludo_completo(nombre,apellido):
    """Imprime un saludo"""
    print('Hola' , nombre, ' ', apellido)

def saludo_generico(nombre='Mundo'):
    """Imprime un saludo"""
    print('Hola' , nombre,)

def cadena_al_revés(nombre='Mundo'):
    """Devuelve una cadena escrita al revés"""
    cadena_invertida = ''
    for char in nombre:
        cadena_invertida = char + cadena_invertida
    return cadena_invertida

def mayusculas(palabra):
    """Devuelve una cadena de texto en mayúsculas"""
    print( palabra.upper() )


# Por último
linea = cadena_al_revés('José Luis Cruz Jaramillo')
print('Así se devuelve después de la función cadena al revés')
print(linea)
print('Así se devuelve después de la función mayúsculas')
mayusculas(linea)