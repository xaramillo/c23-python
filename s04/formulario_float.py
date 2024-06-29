# Formulario Sesión 04

# Agregar elementos numéricos en una lista
variable_lista = []
for i in range(0,2):
    variable = float(input('Agrega un número: '))
    print('el tipo de dato ingresado fue: ', type(variable))
    variable_lista.append(variable)
print('los números fueron: ', variable_lista)