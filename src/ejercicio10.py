################
# Teo Moreno Piccini - @teopatagonico
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
Escribir una función que indique con True si una palabra o
frase ingresada se trata de un palindromo. Palíndromo, es si
se lee igual de derecha a izquierda que de izquierda a derecha.
"""

def es_palindromo(texto):
    """
    Precondiciones: El valor de entrada debe ser una cadena de
    caracteres
    Poscondiciones: El valor de salida debe ser un valor booleano
    """
    texto_invertido=''
    i=-1
    while i>=(-1*len(texto)):
        texto_invertido+=texto[i]
        i-=1
    if texto==texto_invertido:
        palindromo=True
    else:
        palindromo=False
    return palindromo

def principal():
    """
    Esta función es la que se encarga de la parte 'interactiva' del ejercicio
    (La entrada, la llamada al algoritmo y la salida)
    """
    texto=input("Ingrese un texto: ")
    palindromo=es_palindromo(texto)
    if palindromo:
        print(f"{texto} es un palindromo")
    else:
        print(f"{texto} no es un palindromo")

if __name__ == "__main__":
    principal()

