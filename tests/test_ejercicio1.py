################
# Nombre - @usuario_github
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
Se probará la conversión de temperaturas en grados celsius
a grados fahrenheit y viceversa
"""

from src.ejercicio1 import convertir_a_celsius,convertir_a_fahrenheit

def test_convertir_a_celsius():
    """
    Se sabe que 212 °F son 100 °C, se confirmará esto en el
    programa
    """
    celsius=convertir_a_celsius(212)
    assert isinstance(celsius,float)
    assert celsius==100.0

def test_convertir_a_fahrenheit():
    """
    Se sabe que 0 °C son 32 °F, se confirmará esto en el
    programa
    """
    fahrenheit=convertir_a_fahrenheit(0)
    assert isinstance(fahrenheit,float)
    assert fahrenheit==32.0