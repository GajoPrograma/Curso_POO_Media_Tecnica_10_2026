from dominio import Biblioteca, Libro


def main():
    biblioteca = Biblioteca()
    biblioteca.agregar(Libro("L1", "Robótica escolar"))
    biblioteca.agregar(Libro("L2", "Pensamiento lógico"))
    print("1 Listar | 2 Prestar | 3 Devolver | 0 Salir")
    while True:
        try:
            opcion = input("Opción: ").strip()
            if opcion == "0":
                break
            if opcion == "1":
                for codigo, titulo, disponible in biblioteca.catalogo():
                    print(codigo, titulo, "Disponible" if disponible else "Prestado")
            elif opcion in ("2", "3"):
                codigo = input("Código: ").strip()
                if opcion == "2":
                    biblioteca.prestar(codigo)
                else:
                    biblioteca.devolver(codigo)
                print("Operación registrada")
            else:
                print("Opción inválida")
        except ValueError as error:
            print("No se realizó la operación:", error)
        except (EOFError, KeyboardInterrupt):
            print("\nFin de la biblioteca")
            break


if __name__ == "__main__":
    main()
