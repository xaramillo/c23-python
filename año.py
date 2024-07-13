# Este es un repositorio que se compartio en github
 
entrada = input("Hola! Introduce un año: ")
# Antes:
# year1 = int ("entrada")
# Después
year1 = int(entrada) # En este caso, cuando manipulamos variables no se usan las ""
# Las comillas solo se usan cuando definimos cadenas de texto

# Antes
# print = ("escribe cualquier año. ") # Esta función está mal escrita
# Después:
entrada = input("Hola! Introduce otro año: ")
#Antes
#year2 = int ("entrada") # El mismo comentario que la línea de year1
#Después
year2 =int(entrada)

# Antes: Quieres hacer la comparación
"""

input ="year1 == year2 " # Literalmente estás definiendo que input es igual a la cadena de texto
entrada =input(2023 ) # Lit estas capturando un año cualquiera, no 2023, input pide un str
año = input("entrada") # Pidiendo otro año
print("Años transcurridos. año actual - año ") # Si te a imprimir esto, pero no da ningun resultado
entrada.numero(2019) # No tiene sentido porque la var _entrada_ no tiene un método definido como _número_
print = 2030 - año # No se escribe así
exit =(2024)  # No se escribe así    
print("") # Solo imprimiría una cadena vacía

"""

if year1 == year2:
    print('Son los mismos años')
else:
    # Tenemos que calcular la diferencia
    años_transcurridos = year1 - year2
    if años_transcurridos > 0:
        print('Pasaron: ', años_transcurridos, ' años')
    else:
        años_transcurridos = -1 * años_transcurridos
        print('Faltan: ', años_transcurridos ,' años')

    # year1 = 2020, year2 = 2015, 5 años
    # year1 = 2015, year2 = 2020, -5 años