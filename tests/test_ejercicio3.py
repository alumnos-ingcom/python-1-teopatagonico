################
# Nombre - @usuario_github
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
    assert isinstance(resultado,int)
    assert resultado==1

def test_compara_iguales():
    """
    Ambos numeros son iguales
    """
    resultado=compara(42,42)
    assert isinstance(resultado,int)
    assert resultado==0

def test_compara_menor_mayor():
    """
    El primer numero es menor al segundo
    """
    resultado=compara(42,50)
    assert isinstance(resultado,int)
    assert resultado==-1
