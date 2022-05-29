################
# Teo Moreno Piccini - @teopatagonico
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
Se probará el calculo de factores primos de un numero determinado
"""

from src.ejercicio9 import factores_primos

def test_factores_primos():
    """
    Se conoce que los factores primos de 100 son 2 y 5, se probará
    esto en el programa
    """
    resultado=factores_primos(100)
    assert isinstance(resultado,tuple),"El valor debe ser una tupla"
    assert resultado==(2,5),"El valor es incorrecto"
