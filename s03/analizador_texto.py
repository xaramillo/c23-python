# Script en Python que muestra diversas operaciones con strings

# Declaración de cadenas de texto
saludo = "Hola"
nombre = "Mundo"
frase = "  Python es increíble!  "

# Concatenación
mensaje = saludo + ", " + nombre + "!"
print("Concatenación:", mensaje)

# Repetición
repetir = saludo * 3
print("Repetición:", repetir)

# Longitud de una cadena
longitud = len(frase)
print("Longitud de la cadena 'frase':", longitud)

# Acceso a caracteres
primer_caracter = saludo[0]
ultimo_caracter = saludo[-1]
print("Primer carácter de 'saludo':", primer_caracter)
print("Último carácter de 'saludo':", ultimo_caracter)

# Subcadenas (slicing)
subcadena = frase[2:8]
print("Subcadena de 'frase':", subcadena)

# Métodos de cadenas
mayusculas = frase.upper()
minusculas = frase.lower()
titulo = frase.title()
sin_espacios = frase.strip()
reemplazo = frase.replace("increíble", "asombroso")

print("Mayúsculas:", mayusculas)
print("Minúsculas:", minusculas)
print("Formato título:", titulo)
print("Sin espacios en blanco:", sin_espacios)
print("Reemplazo de palabras:", reemplazo)

# División de cadenas
palabras = frase.split()
print("División en palabras:", palabras)

# Verificación de contenido
empieza_con = frase.startswith("Python")
termina_con = frase.endswith("increíble!")
contiene = "es" in frase

print("¿Empieza con 'Python'?:", empieza_con)
print("¿Termina con 'increíble!'?:", termina_con)
print("¿Contiene 'es'?:", contiene)

# Formateo de cadenas
formato1 = f"{saludo}, {nombre}! Bienvenido a Python."
formato2 = "{}. ¡Es un placer conocerte, {}!".format(saludo, nombre)
formato3 = "%s, %s! Disfruta programando en Python." % (saludo, nombre)

print("Formateo con f-string:", formato1)
print("Formateo con format:", formato2)
print("Formateo con %:", formato3)