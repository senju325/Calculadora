"""Funciones matemáticas de la calculadora.

Cada función recibe números ya validados y devuelve el resultado.
Si la operación no es posible (por ejemplo, dividir entre cero),
lanza ValueError con un mensaje claro para el usuario.
"""

import math


def sumar(a, b):
    return a + b


def restar(a, b):
    return a - b


def multiplicar(a, b):
    return a * b


def dividir(a, b):
    if b == 0:
        raise ValueError("no se puede dividir entre cero.")
    return a / b


def potencia(base, exponente):
    if base == 0 and exponente < 0:
        raise ValueError("0 no se puede elevar a un exponente negativo.")
    if base < 0 and not float(exponente).is_integer():
        raise ValueError("una base negativa no admite exponentes con decimales.")
    return base ** exponente


def modulo(a, b):
    if b == 0:
        raise ValueError("no se puede calcular el módulo con divisor cero.")
    return a % b


def raiz_cuadrada(numero):
    if numero < 0:
        raise ValueError("no existe la raíz cuadrada real de un número negativo.")
    return math.sqrt(numero)


def porcentaje(porcentaje, cantidad):
    return cantidad * porcentaje / 100


def valor_absoluto(numero):
    return abs(numero)


def factorial(n):
    if n < 0:
        raise ValueError("el factorial solo existe para enteros no negativos.")
    if n > 1000:
        raise ValueError("el número es demasiado grande (máximo 1000).")
    resultado = 1
    for i in range(2, n + 1):
        resultado *= i
    return resultado


def promedio(numeros):
    if not numeros:
        raise ValueError("se necesita al menos un número para el promedio.")
    return sum(numeros) / len(numeros)
