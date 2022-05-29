################
# Teo Moreno Piccini - @teopatagonico
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
Se probará la comparación de dos numeros enteros
"""

from src.ejercicio3 import compara

def test_compara_mayor_menor():
    """
    El primer numero es mayor al segundo
    """
    resultado=compara(50,42)
    assert isinstance(resultado,int),"El valor debe ser un numero entero"
    assert resultado==1,"El valor es incorrecto"

def test_compara_iguales():
    """
    Ambos numeros son iguales
    """
    resultado=compara(42,42)
    assert isinstance(resultado,int),"El valor debe ser un numero entero"
    assert resultado==0,"El valor es incorrecto"

def test_compara_menor_mayor():
    """
    El primer numero es menor al segundo
    """
    resultado=compara(42,50)
    assert isinstance(resultado,int),"El valor debe ser un numero entero"
    assert resultado==-1,"El valor es incorrecto"
