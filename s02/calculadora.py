# Demo 1: Sintaxis de Python para creación de Scripts
# MODO CALCULADORA

# Variables y tipos de datos que usaremos como Constantes
num = 42            # Entero
pi = 3.14159        # Flotante
pyname = "Python"     # Cadena de texto
is_valid = True     # Booleano

# Funciones
def greet(name=pyname):
    return f"Hola, {name}!"
# Ejemplo práctico
def calcular_operaciones(numero1, numero2):
    suma = numero1 + numero2
    resta = numero1 - numero2
    multiplicacion = numero1 * numero2
    division = numero1 / numero2 if numero2 != 0 else "División por cero no permitida"
    
    return suma, resta, multiplicacion, division

def dividir_a_pi(num=num):
    
    return(pi/num)

num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))

greet()
resultados = calcular_operaciones(num1, num2)
print(f"Suma: {resultados[0]}")
print(f"Resta: {resultados[1]}")
print(f"Multiplicación: {resultados[2]}")
print(f"División: {resultados[3]}")

