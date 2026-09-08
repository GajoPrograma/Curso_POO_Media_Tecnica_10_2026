"""Operaciones sin lectura de teclado: fáciles de probar por separado."""
import math


def calcular(a, operador, b):
    if type(a) not in (int, float) or type(b) not in (int, float):
        raise ValueError("Los operandos deben ser números")
    if not math.isfinite(a) or not math.isfinite(b):
        raise ValueError("Usa números finitos")
    if operador == "+":
        resultado = a + b
    elif operador == "-":
        resultado = a - b
    elif operador == "*":
        resultado = a * b
    elif operador == "/":
        if b == 0:
            raise ZeroDivisionError("No se puede dividir por cero")
        resultado = a / b
    else:
        raise ValueError("Operador desconocido")
    if not math.isfinite(resultado):
        raise ValueError("Resultado fuera del rango admitido")
    return resultado
