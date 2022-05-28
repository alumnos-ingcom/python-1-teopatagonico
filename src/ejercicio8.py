################
# Teo Moreno Piccini - @teopatagonico
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
Escribir una función que indique con `True`
si un numero indicado es Primo.
"""

def es_primo(numero):
    """
    Precondiciones: El numero debe ser un entero positivo
    Poscondiciones: El valor retornado debe ser de tipo booleano,
    el calculo debe ser realizado correctamente
    """
    primo=True
    i=2
    while i<numero:
        if numero%i==0:
            primo=False
            i=numero
        i+=1
    return primo
    pass

def principal():
    """
    Esta función es la que se encarga de la parte 'interactiva' del ejercicio
    (La entrada, la llamada al algoritmo y la salida)
    """
    numero=int(input("Ingrese un número entero positivo: "))
    primo=es_primo(numero)
    if primo:
        print(f"El numero {numero} es primo")
    else:
        print(f"El numero {numero} no es primo")

if __name__ == "__main__":
    principal()

