################
# Teo Moreno Piccini - @teopatagonico
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
Se probará la extracción de signos de números enteros.
"""

from src.ejercicio2 import signo

def test_signo_positivo():
    """
    El valor de entrada es un número positivo
    """
    resultado=signo(42)
    assert isinstance(resultado,int),"El valor debe ser un numero entero"
    assert resultado==1,"El valor es incorrecto"

def test_signo_cero():
    """
    El valor de entrada es cero
    """
    resultado=signo(0)
    assert isinstance(resultado,int),"El valor debe ser un numero entero"
    assert resultado==0,"El valor es incorrecto"

def test_signo_negativo():
    """
    El valor de entrada es un número negativo
    """
    resultado=signo(-42)
    assert isinstance(resultado,int),"El valor debe ser un numero entero"
    assert resultado==-1,"El valor es incorrecto"
