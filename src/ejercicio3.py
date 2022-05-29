################
# Teo Moreno Piccini - @teopatagonico
#UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
Escribir una función que utilizando sumas y restas, reciba dos valores y retorne:

- Retornar `-1` si el primero es menor que el segundo
- Retornar `0` si son iguales
- Retornar `1` si el primero es mayor que el segundo
"""

def compara(numero,otro_numero):
    """
    Precondiciones: Los valores de entrada deben ser
    numeros enteros
    Poscondiciones: El valor de salida debe ser un numero
    entero entre -1 y 1
    """
    seguir=True
    while seguir:
        if numero>0:
            if otro_numero>0:
                numero-=1
                otro_numero-=1
            else:
                resultado=1
                seguir=False
        else:
            if otro_numero>0:
                resultado=-1
                seguir=False
            else:
                resultado=-0
                seguir=False
    return resultado
def principal():
    """
    Esta función es la que se encarga de la parte 'interactiva' del ejercicio
    (La entrada, la llamada al algoritmo y la salida)
    """
    numero_1=int(input("Ingrese un número: "))
    numero_2=int(input("Ingrese otro número: "))
    resultado=compara(numero_1,numero_2)
    print(f"El resultado de la comparación es {resultado}")

if __name__ == "__main__":
    principal()
