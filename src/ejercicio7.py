################
# Teo Moreno Piccini - @teopatagonico
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
Escribir un programa que permita transformar un número solicitado
expresado en grados, minutos y segundos a segundos a segundos.
Y otra que haga el cambio en el sentido contrario,
devolviendo una `tuple`.
"""

def sexadecimal_a_decimal(horas, minutos, segundos):
    """
    Precondiciones: El numero de horas debe ser mayor o igual a 0,
    minutos debe ser un numero entero entre 0 y 60, el numero de
    segundos debe ser un numero entero entre 0 y 60
    Poscondiciones: Los segundos deben ser mayores o iguales a cero
    """
    minutos+=horas*60
    segundos+=minutos*60
    return segundos

def decimal_a_sexadecimal(numero):
    """
    Precondiciones: El numero de segundos debe ser un numero entero
    mayor o igual a 0
    Poscondiciones: Los numeros deben ser mayores a cero, los minutos
    y segundos deben ser menores a sesenta
    """
    segundos=numero
    minutos=0
    while segundos>=60:
        minutos+=1
        segundos-=60
    horas=0
    while minutos>=60:
        horas+=1
        minutos-=60
    return (horas,minutos,segundos)

def principal():
    """
    Esta función es la que se encarga de la parte 'interactiva' del ejercicio
    (La entrada, la llamada al algoritmo y la salida)
    """
    segundos_deci=int(input("Ingrese un numero en segundos: "))
    horas,minutos,segundos_sexa=decimal_a_sexadecimal(segundos_deci)
    print(f"{segundos_deci} segundos son {horas} horas, {minutos} minutos y {segundos_sexa} segundos.")
    segundos_deci=sexadecimal_a_decimal(horas,minutos,segundos_sexa)
    print(f"{horas} horas, {minutos} minutos y {segundos_sexa} segundos son {segundos_deci} segundos.")

if __name__ == "__main__":
    principal()

