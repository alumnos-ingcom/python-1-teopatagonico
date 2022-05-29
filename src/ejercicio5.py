################
# Teo Moreno Piccini - @teopatagonico
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
Escribir una función que mediante restas sucesivas, obtenga el valor del
cociente y resto de dos números enteros.
"""

try:
    from ejercicio2 import signo
except ImportError:
    from src.ejercicio2 import signo

def division_lenta(dividendo,divisor):
    """
    Precondiciones: Ambos números deben ser enteros
    Poscondiciones: Ambos números deben ser enteros
    """
    cociente=0
    dividir=True
    signo_dividendo=signo(dividendo)
    signo_divisor=signo(divisor)
    dividendo=abs(dividendo)
    divisor=abs(divisor)
    if divisor==0:
        dividir=False
        cociente="Indefinido"
        resto="Indefinido"
    else:
        while dividir:
            if dividendo-divisor>=0:
                cociente+=1
                dividendo-=divisor
            else:
                resto=dividendo
                dividir=False
        if signo_dividendo!=signo_divisor:
            cociente=cociente*-1
            resto=resto*-1
    return cociente,resto

def principal():
    """
    Esta función es la que se encarga de la parte 'interactiva' del ejercicio
    (La entrada, la llamada al algoritmo y la salida)
    """
    dividendo=int(input("Ingrese un numero: "))
    divisor=int(input("Ingrese otro numero: "))
    cociente,resto=division_lenta(dividendo,divisor)
    print(f"El cociente entre {dividendo} y {divisor} es {cociente}, con resto {resto}")

if __name__ == "__main__":
    principal()
