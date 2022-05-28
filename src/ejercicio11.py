################
# Teo Moreno Piccini - @teopatagonico
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
Escribir una función que indique con `True` si un número entero
es multiplo de otro, utilizando sumas y restas.
"""

from ejercicio5 import division_lenta

def es_multiplo(numero, multiplo):
    """
    Precondiciones: Los numeros deben ser enteros
    Poscondiciones: La salida debe ser un booleano
    """
    resto=division_lenta(numero,multiplo)[1]
    return resto==0

def principal():
    """
    Esta función es la que se encarga de la parte 'interactiva' del ejercicio
    (La entrada, la llamada al algoritmo y la salida)
    """
    numero=int(input("Ingrese un numero entero: "))
    multiplo=int(input("Ingrese otro numero entero: "))
    resultado=es_multiplo(numero,multiplo)
    if resultado:
        print(f"{numero} es multiplo de {multiplo}")
    else:
        print(f"{numero} no es multiplo de {multiplo}")

if __name__ == "__main__":
    principal()
