################
# Teo Moreno Piccini - @teopatagonico
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
Se probará el ordenamiento de un conjunto de numeros
"""

from src.ejercicio6 import ordenar_mayor_a_menor,ordenar_menor_a_mayor

def test_ordenar_mayor_a_menor():
    """
    Los numeros son 15, 2 y 42
    """
    resultado=ordenar_mayor_a_menor(15,2,42)
    assert isinstance(resultado,tuple),"El resultado debe ser una tupla"
    assert resultado==(42,15,2),"El resultado es incorrecto"

def test_ordenar_menor_a_mayor():
    """
    Los numeros son 15, 2 y 42
    """
    resultado=ordenar_menor_a_mayor(15,2,42)
    assert isinstance(resultado,tuple),"El resultado debe ser una tupla"
    assert resultado==(2,15,42),"El resultado es incorrecto"
