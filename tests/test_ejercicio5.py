################
# Teo Moreno Piccini - @teopatagonico
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
Se probará la división lenta con numeros de signo arbitrario
"""

from src.ejercicio5 import division_lenta

def test_division_lenta_ambos_positivos():
    """
    Ambos valores son positivos
    """
    resultado=division_lenta(10,2)
    assert isinstance(resultado,tuple),"El valor debe ser una tupla"
    cociente=10//2
    resto=10%2
    assert resultado[0]==cociente,"El cociente es incorrecto"
    assert resultado[1]==resto,"El resto es incorrecto"

def test_division_lenta_ambos_negativos():
    """
    Ambos valores son negativos
    """
    resultado=division_lenta(-10,-2)
    assert isinstance(resultado,tuple),"El valor debe ser una tupla"
    cociente=-10//-2
    resto=-10%-2
    assert resultado[0]==cociente,"El cociente es incorrecto"
    assert resultado[1]==resto,"El resto es incorrecto"

def test_division_lenta_positivo_negativo():
    """
    El dividendo es positivo y el divisor es negativo
    """
    resultado=division_lenta(10,-2)
    assert isinstance(resultado,tuple),"El valor debe ser una tupla"
    cociente=10//-2
    resto=10%-2
    assert resultado[0]==cociente,"El cociente es incorrecto"
    assert resultado[1]==resto,"El resto es incorrecto"

def test_division_lenta_negativo_positivo():
    """
    El dividendo es negativo y el divisor es positivo
    """
    resultado=division_lenta(10,-2)
    assert isinstance(resultado,tuple),"El valor debe ser una tupla"
    cociente=-10//2
    resto=-10%2
    assert resultado[0]==cociente,"El cociente es incorrecto"
    assert resultado[1]==resto,"El resto es incorrecto"

def test_division_lenta_divisor_0():
    """
    El dividendo es positivo y el divisor es negativo
    """
    resultado=division_lenta(10,0)
    assert isinstance(resultado,tuple),"El valor debe ser una tupla"
    cociente="Indefinido"
    resto="Indefinido"
    assert resultado[0]==cociente,"El cociente es incorrecto"
    assert resultado[1]==resto,"El resto es incorrecto"
