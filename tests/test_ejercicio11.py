################
# Teo Moreno Piccini - @teopatagonico
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
Se probará la verificación de la multiplicidad de dos numeros
"""

from src.ejercicio11 import es_multiplo

def test_es_multiplo():
    """
    Se conoce que 100 es multiplo de 5, se probara esto en el
    programa
    """
    resultado=es_multiplo(100,5)
    assert isinstance(resultado,bool),"El valor debe ser un booleano"
    assert resultado==True,"El valor es incorrecto"
