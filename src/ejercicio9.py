################
# Teo Moreno Piccini - @teopatagonico
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
Escribir una función que retorne una `tuple` con factores
primos de un numero entero positivo.
"""

try:
    from ejercicio8 import es_primo
except ImportError:
    from src.ejercicio8 import es_primo

def factores_primos(numero):
    """
    Precondiciones: El numero debe ser un entero positivo
    Poscondiciones: El resultado debe ser una tupla, los
    elementos de la tupla deben ser enteros positivos.
    """
    factores=[]
    i=2
    while i<numero:
        if numero%i==0:
            factores.append(i)
        i+=1
    factores_primos=[]
    i=0
    while i<len(factores):
        factor=factores[i]
        if es_primo(factor):
            factores_primos.append(factor)
        i+=1
    factores_primos=tuple(factores_primos)
    return factores_primos

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
