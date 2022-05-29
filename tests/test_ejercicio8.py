################
# Teo Moreno Piccini - @teopatagonico
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
Se probará el calculo de un numero primo
"""

from src.ejercicio8 import es_primo

def test_es_primo():
    """
    Se sabe que el numero 13 es primo, se probará esto en el
    programa
    """
    resultado=es_primo(13)
    assert isinstance(resultado,bool),"El valor debe ser un booleano"
    assert resultado==True,"El valor es incorrecto"
