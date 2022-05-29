################
# Teo Moreno Piccini - @teopatagonico
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
Se probará la conversion desde el sistema sexagesimal al decimal
"""

from src.ejercicio7 import decimal_a_sexadecimal,sexadecimal_a_decimal

def test_decimal_a_sexadecimal():
    """
    Se conoce que 3661 segundos son 1 hora, 1 minuto y 1 segundo,
    se confirmara esto en el programa
    """
    resultado=decimal_a_sexadecimal(3661)
    assert isinstance(resultado,tuple),"El valor debe ser una tupla"
    assert resultado==(1,1,1),"El valor es incorrecto"

def test_sexadecimal_a_decimal():
    """
    Se conoce que 5 horas son 18000 segundos, se confirmara esto
    en el programa
    """
    resultado=sexadecimal_a_decimal(5,0,0)
    assert isinstance(resultado,int),"El resultado debe ser un entero"
    assert resultado==18000,"El resultado es incorrecto"
