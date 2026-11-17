"""Calculadora: menú, lectura de datos y presentación de resultados."""

import operaciones as op


def leer_numero(mensaje):
    return float(input(mensaje))


def formatear(numero):
    """Muestra 5.0 como 5 y evita colas como 0.30000000000000004."""
    if isinstance(numero, int):
        return str(numero)
    if numero.is_integer() and abs(numero) < 1e15:
        return str(int(numero))
    if abs(numero) >= 1e15 or abs(numero) < 1e-6:
        return f"{numero:.6e}"
    return str(round(numero, 10))


# --- Operaciones: cada una pide sus datos y devuelve (expresión, resultado) ---

def pedir_suma():
    a = leer_numero("  Primer número: ")
    b = leer_numero("  Segundo número: ")
    return f"{formatear(a)} + {formatear(b)}", op.sumar(a, b)


def pedir_resta():
    a = leer_numero("  Primer número: ")
    b = leer_numero("  Segundo número: ")
    return f"{formatear(a)} - {formatear(b)}", op.restar(a, b)


def pedir_multiplicacion():
    a = leer_numero("  Primer número: ")
    b = leer_numero("  Segundo número: ")
    return f"{formatear(a)} × {formatear(b)}", op.multiplicar(a, b)


def pedir_division():
    a = leer_numero("  Dividendo: ")
    b = leer_numero("  Divisor: ")
    return f"{formatear(a)} ÷ {formatear(b)}", op.dividir(a, b)


# Opción del menú -> (grupo, nombre, función que la ejecuta)
OPERACIONES = {
    "1": ("Básicas", "Suma", pedir_suma),
    "2": ("Básicas", "Resta", pedir_resta),
    "3": ("Básicas", "Multiplicación", pedir_multiplicacion),
    "4": ("Básicas", "División", pedir_division),
}


def mostrar_menu():
    print("\n" + "=" * 34)
    print("          CALCULADORA")
    print("=" * 34)
    grupo_actual = None
    for clave, (grupo, nombre, _) in OPERACIONES.items():
        if grupo != grupo_actual:
            print(f"\n {grupo}")
            grupo_actual = grupo
        print(f"  {clave:>2}. {nombre}")
    print("\n   0. Salir")
    print("=" * 34)


def main():
    print("Bienvenido a la calculadora.")
    while True:
        mostrar_menu()
        opcion = input("Elige una opción: ").strip().lower()

        if opcion == "0":
            break
        if opcion not in OPERACIONES:
            print("  Opción no válida. Elige una del menú.")
            continue

        _, nombre, ejecutar = OPERACIONES[opcion]
        print(f"\n-- {nombre} --")
        expresion, resultado = ejecutar()
        print(f"  Resultado: {expresion} = {formatear(resultado)}")

    print("¡Hasta luego!")


if __name__ == "__main__":
    main()
