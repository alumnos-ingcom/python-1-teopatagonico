################
# Teo Moreno Piccini - @teopatagonico
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
Escribir una función que retorne una `tuple` con factores
primos de un numero entero positivo.
"""

from ejercicio8 import es_primo

def factores_primos(numero):
    """
    Precondiciones: El numero debe ser un entero positivo
    Poscondiciones: El resultado debe ser una tupla, los
    elementos de la tupla deben ser enteros positivos.
    """
    divisores=[]
    i=2
    while i<numero:
        if numero%i==0:
            divisores.append(i)
        i+=1
    divisores_primos=[]
    i=0
    while i<len(divisores):
        divisor=divisores[i]
        if es_primo(divisor):
            divisores_primos.append(divisor)
        i+=1
    divisores_primos=tuple(divisores_primos)
    return divisores_primos

def principal():
    """
    Esta función es la que se encarga de la parte 'interactiva' del ejercicio
    (La entrada, la llamada al algoritmo y la salida)
    """
    numero=int(input("Ingrese un numero entero positivo: "))
    resultado=factores_primos(numero)
    print(f"Los divisores primos de {numero} son {resultado}")

if __name__ == "__main__":
    principal()

