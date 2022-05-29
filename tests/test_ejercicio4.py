################
# Teo Moreno Piccini - @teopatagonico
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
Se probará la suma lenta de numeros de signo arbitrario.
"""

from src.ejercicio4 import suma_lenta

def test_suma_lenta_ambos_positivos():
    """
    Ambos valores de entrada son numeros positivos
    """
    resultado=suma_lenta(42,6)
    assert isinstance(resultado,int),"El resultado debe ser un número entero"
    suma=42+6
    assert resultado==suma,"Suma incorrecta"

def test_suma_lenta_ambos_negativos():
    """
    Ambos valores de entrada son numeros negativos
    """
    resultado=suma_lenta(-42,-6)
    assert isinstance(resultado,int),"El resultado debe ser un número entero"
    suma=-42-6
    assert resultado==suma,"Suma incorrecta"

def test_suma_lenta_positivo_negativo():
    """
    El valor 1 es positivo, el valor 2 es negativo
    """
    resultado=suma_lenta(42,-6)
    assert isinstance(resultado,int),"El resultado debe ser un número entero"
    suma=42-6
    assert resultado==suma,"Suma incorrecta"

def test_suma_lenta_negativo_positivo():
    """
    El valor 1 es negativo, el valor 2 es positivo
    """
    resultado=suma_lenta(-42,6)
    assert isinstance(resultado,int),"El resultado debe ser un número entero"
    suma=-42+6
    assert resultado==suma,"Suma incorrecta"
