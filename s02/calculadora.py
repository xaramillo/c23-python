# Demo 1: Sintaxis de Python para creación de Scripts
# MODO CALCULADORA

# Variables y tipos de datos que usaremos como Constantes
NUM = 42            # Entero
PI = 3.14159        # Flotante
PYNAME = "Python"     # Cadena de texto
IS_VALID = True     # Booleano

# Funciones
def greet(name = PYNAME):
    """Devuelve un saludo."""
    return f"Hola, {name}!"

# Ejemplo práctico
def calcular_operaciones(numero1, numero2):
    """Hace cálculos con dos números dados."""
    suma = numero1 + numero2
    resta = numero1 - numero2
    multiplicacion = numero1 * numero2
    division = numero1 / numero2 if numero2 != 0 else "División por cero no permitida"
    
    return suma, resta, multiplicacion, division

# Devuelve flotante de PI y num
def dividir_a_pi(num=NUM):
    """Divide a PI entre el numero dado.
       El numero dado es una constante definida al principio.
       si se necesita se puede cambiar la ejecución con otro num.
    """
    return(PI/num)

# Inicio de la ejecución

num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))

greet()
resultados = calcular_operaciones(num1, num2)

print(f"Suma: {resultados[0]}")
print(f"Resta: {resultados[1]}")
print(f"Multiplicación: {resultados[2]}")
print(f"División: {resultados[3]}")

