################
# Teo Moreno Piccini - @teopatagonico
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
Se probará el reconocimiento de palindromos en el programa
"""

from src.ejercicio10 import es_palindromo

def test_es_palindromo():
    """
    Se conoce que 'aibofobia' es un palindromo, se probará
    esto en el programa
    """
    resultado=es_palindromo('aibofobia')
    assert isinstance(resultado,bool),"El valor debe ser un booleano"
    assert resultado==True,"El valor es incorrecto"
