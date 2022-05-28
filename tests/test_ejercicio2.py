################
# Nombre - @usuario_github
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
    assert isinstance(resultado,int)
    assert resultado==1

def test_signo_cero():
    """
    El valor de entrada es cero
    """
    resultado=signo(0)
    assert isinstance(resultado,int)
    assert resultado==0

def test_signo_negativo():
    """
    El valor de entrada es un número negativo
    """
    resultado=signo(-42)
    assert isinstance(resultado,int)
    assert resultado==-1
