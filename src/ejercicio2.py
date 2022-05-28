################
# Teo Moreno Piccini - @teopatagonico
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
Escribir una función que reciba un número e indique si el
mismo es positivo, negativo o cero utilizando sumas y restas.
"""

def signo(numero):
    """
    Precondiciones: El valor de entrada debe ser un numero entero
    Poscondiciones: El valor de salida debe ser un numero entero
    entre -1 y 1
    """
    contador=numero
    i=0
    while i<numero:
        contador=contador-1
        i+=1
    while i>numero:
        contador=contador-1
        i-=1
    if i==0:
        signo=0
    else:
        if contador==0:
            signo=1
        else:
            signo=-1
    return signo

def principal():
    """
    Esta función es la que se encarga de la parte 'interactiva' del ejercicio
    (La entrada, la llamada al algoritmo y la salida)
    """
    numero=int(input("Ingrese un número entero: "))
    signo_numero=signo(numero)
    print(f"El signo de {numero} es {signo_numero}.")

if __name__ == "__main__":
    principal()
