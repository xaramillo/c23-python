estudiantes = [
    ("Ana", 85),
    ("Luis", 78),
    ("Carlos", 92),
    ("Marta", 59),
    ("Sofía", 74),
    ("Pedro", 41),
    ("Elena", 65),
    ("Jorge", 53),
    ("María", 88),
    ("Juan", 77),
    ("Paula", 95),
    ("Fernando", 61),
    ("Laura", 80),
    ("Sergio", 57),
    ("Patricia", 62),
    ("Raúl", 70),
    ("Isabel", 93),
    ("Andrés", 45),
    ("Silvia", 55),
    ("Ricardo", 60),
    ("Gabriela", 83),
    ("Hugo", 49),
    ("Natalia", 68),
    ("Tomás", 90),
    ("Lorena", 72),
    ("Miguel", 50),
    ("Daniela", 81),
    ("Iván", 67),
    ("Adriana", 76),
    ("Enrique", 58)
]

# Filtrar las calificaciones en estudiantes que aprobaron y reprobaron
umbral = 60

for tupla in estudiantes:
    print('elemento: ', tupla)
    print('\tNombre: ', tupla[0])
    print('\tCalif: ', tupla[1])

# Lista de comprehensión

# Iterable: estudiantes
# Elemento: tupla
# Expresión: nombre
# Condición: Sí, calificacion > 60

aprobados = [ tupla[0] for tupla in estudiantes if tupla[1] >= umbral ]
reprobados = [ tupla[0] for tupla in estudiantes if tupla[1] < umbral ]

print(f"Alumnos aprobados: {aprobados}")
print('\n')
print(f"Alumnos reprobados: {reprobados}")

# Hacer un diccionario con los estudiantes y sus calificaciones

# Iterable: estudiantes
# Elemento: nombre, calif
# Expresión: calif
# Clave: nombre
# Valor: calif
# Condición: No

print([ calif for nombre, calif in estudiantes ])

# {clave: valor for elemento in iterable}
diccionario_estudiantes ={nombre : calif for nombre, calif in estudiantes}

print(diccionario_estudiantes)
# Cálculo de estadisticas generales