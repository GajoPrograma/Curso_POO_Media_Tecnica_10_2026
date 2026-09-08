from operaciones import calcular


def main():
    print("Calculadora: +, -, *, /. Escribe salir como operador para terminar.")
    while True:
        try:
            operador = input("Operador: ").strip()
            if operador == "salir":
                break
            a = float(input("Primer número: "))
            b = float(input("Segundo número: "))
            print("Resultado:", calcular(a, operador, b))
        except (ValueError, ZeroDivisionError) as error:
            print("No se realizó la operación:", error)
        except (EOFError, KeyboardInterrupt):
            print("\nFin de la calculadora")
            break


if __name__ == "__main__":
    main()
