################
# Teo Moreno Piccini - @teopatagonico
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
Se quiere transformar temperaturas en grados fahrenheit a grados centígrados y viceversa.

Escribir las funciones para convertir la temperatura en grados centigrados en fahrenheit como
un número decimal, utilice esta formula para calcular los grados centígrados y retorne el
resultado obtenido. Y viceversa.
"""

def convertir_a_fahrenheit(centigrados):
    """
    Precondiciones: El valor de entrada debe ser un numero
    Poscondiciones: El valor de salida debe ser un numero
    """
    fahrenheit = 1.8 * centigrados + 32.0
    return fahrenheit

def convertir_a_celsius(fahrenheit):
    """
    Precondiciones: El valor de entrada debe ser un numero
    Poscondiciones: El valor de salida debe ser un numero
    """
    celsius = (fahrenheit - 32.0) / 1.8
    return celsius

def principal():
    """
    Esta función es la que se encarga de la parte 'interactiva' del ejercicio
    (La entrada, la llamada al algoritmo y la salida)
    """
    celsius_usuario=input("Ingrese un valor en grados celsius: ")
    celsius_1=int(celsius_usuario)
    fahrenheit=convertir_a_fahrenheit(celsius_1)
    print(f"{celsius_1} grados celsius son {fahrenheit} grados fahrenheit.")
    celsius_2=convertir_a_celsius(fahrenheit)
    print(f"{fahrenheit} grados celsius son {celsius_2} grados celsius.")
    if celsius_1==celsius_2:
        print("La conversión fue realizada correctamente")
    else:
        print("Hubo un error en la conversión")

if __name__ == "__main__":
    principal()
