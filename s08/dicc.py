# Definición de un diccionario

diccionario = { 
  "clave" : "valor",
  "clave2" : 2134,
  "clave3" : True,
  "clave4": [1,2,3],
  "clave5" : "palabra"
 }

# Métodos de acceso
# Selección por clave
print('Selección por clave')
print(diccionario["clave"])

# Selección de todas las claves
print('Selección de todas las claves por el método .keys()')
print(diccionario.keys())

# Selección de todos los valores
print('Selección de todas los valores por el método .items()')
print(diccionario.items())

# Selección de todos los valores
print('Selección de todas los resultados por el método .values()')
print(diccionario.values())
