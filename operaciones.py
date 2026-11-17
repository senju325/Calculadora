"""Funciones matemáticas de la calculadora.

Cada función recibe números ya validados y devuelve el resultado.
Si la operación no es posible (por ejemplo, dividir entre cero),
lanza ValueError con un mensaje claro para el usuario.
"""


def sumar(a, b):
    return a + b


def restar(a, b):
    return a - b


def multiplicar(a, b):
    return a * b


def dividir(a, b):
    return a / b


def potencia(base, exponente):
    if base == 0 and exponente < 0:
        raise ValueError("0 no se puede elevar a un exponente negativo.")
    if base < 0 and not float(exponente).is_integer():
        raise ValueError("una base negativa no admite exponentes con decimales.")
    return base ** exponente
