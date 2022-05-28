################
# Teo Moreno Piccini - @teopatagonico
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
Escribir una función que haga la suma entre dos números enteros sin hacer la operación de
manera directa. Esto quiere decir que para hacer la suma entre 4 y 3, las operaciones
resultantes deberán ser 4+1+1+1.

La funcion debe ser capaz de sumar cualquier numero entero positivo y negativo.
"""

from ejercicio2 import signo

def suma_lenta(numero,otro_numero):
    """
    Precondiciones: Ambos numeros deben ser enteros
    Poscondiciones: El resultado debe ser la suma correcta de los numeros ingresados
    """
    resultado=numero
    direccion=signo(otro_numero)
    i=0
    while i < abs(otro_numero):
        resultado+=1*direccion
        i += 1
    return resultado

def principal():
    """
    Esta función es la que se encarga de la parte 'interactiva' del ejercicio
    (La entrada, la llamada al algoritmo y la salida)
    """
    numero=int(input("Ingrese un numero entero: "))
    otro_numero=int(input("Ingrese otro numero entero: "))
    resultado=suma_lenta(numero,otro_numero)
    print(f"La suma de {numero} + {otro_numero} es igual a {resultado}")

if __name__ == "__main__":
    principal()
