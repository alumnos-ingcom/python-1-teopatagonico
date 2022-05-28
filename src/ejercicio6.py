################
# Teo Moreno Piccini - @teopatagonico
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
Escribir una función que a partir de tres variables de tipo
entero retorne una tupla con dichos valores ordenados de
menor a mayor. Y Viceversa.
"""

from ejercicio3 import compara

def ordenar_mayor_a_menor(uno, dos, tres):
    """
    Precondiciones: Los valores de entrada deben ser numeros
    enteros
    Poscondiciones: El valor de salida debe ser una tupla,
    los elementos de la tupla deben estar ordenados
    """
    if compara(tres,dos)==1:
        tres,dos=dos,tres
    if compara(dos,uno)==1:
        dos,uno=uno,dos
    if compara(tres,dos)==1:
        tres,dos=dos,tres
    return (uno,dos,tres)

def ordenar_menor_a_mayor(uno, dos, tres):
    """
    Precondiciones: Los valores de entrada deben ser numeros
    enteros
    Poscondiciones: El valor de salida debe ser una tupla,
    los elementos de la tupla deben estar ordenados
    """
    if compara(tres,dos)==-1:
        tres,dos=dos,tres
    if compara(dos,uno)==-1:
        dos,uno=uno,dos
    if compara(tres,dos)==-1:
        tres,dos=dos,tres
    return (uno,dos,tres)

def principal():
    """
    Esta función es la que se encarga de la parte 'interactiva' del ejercicio
    (La entrada, la llamada al algoritmo y la salida)
    """
    uno=int(input("Ingrese el primer numero: "))
    dos=int(input("Ingrese el segundo numero: "))
    tres=int(input("Ingrese el tercer numero: "))
    mayor_menor=ordenar_mayor_a_menor(uno,dos,tres)
    menor_mayor=ordenar_menor_a_mayor(uno,dos,tres)
    print(f"Ordenados de mayor a menor: {mayor_menor}")
    print(f"Ordenados de menor a mayor: {menor_mayor}")

if __name__ == "__main__":
    principal()
