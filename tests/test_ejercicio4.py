################
# Nombre - @usuario_github
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
