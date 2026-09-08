from pathlib import Path

from dominio import Inventario
from persistencia import cargar, guardar

RUTA = Path(__file__).resolve().parent / "datos_locales" / "inventario.json"


def main():
    try:
        inventario = cargar(RUTA)
    except FileNotFoundError:
        inventario = Inventario()
        print("Primer uso: inventario vacío")
    except (ValueError, OSError) as error:
        print("No se pudo cargar el archivo:", error)
        print("Revisa o recupera el archivo antes de continuar:", RUTA)
        return

    pendiente = False
    print("1 Listar | 2 Agregar | 3 Ingresar | 4 Retirar | 5 Guardar | 0 Salir")
    while True:
        try:
            opcion = input("Opción: ").strip()
            if opcion == "0":
                if pendiente:
                    decision = input("Hay cambios sin guardar. ¿Descartarlos? si/no: ").strip().lower()
                    if decision != "si":
                        continue
                break
            if opcion == "1":
                filas = inventario.listar()
                if not filas:
                    print("Inventario vacío")
                for fila in filas:
                    print(fila["codigo"], fila["nombre"], fila["cantidad"])
            elif opcion == "2":
                codigo = input("Código: ")
                nombre = input("Nombre: ")
                cantidad = int(input("Cantidad inicial: "))
                inventario.agregar(codigo, nombre, cantidad)
                pendiente = True
                print("Material agregado; recuerda guardar")
            elif opcion in ("3", "4"):
                codigo = input("Código: ")
                cantidad = int(input("Cantidad del movimiento: "))
                if opcion == "3":
                    inventario.ingresar(codigo, cantidad)
                else:
                    inventario.retirar(codigo, cantidad)
                pendiente = True
                print("Movimiento registrado; recuerda guardar")
            elif opcion == "5":
                guardar(inventario, RUTA)
                pendiente = False
                print("Guardado en", RUTA)
            else:
                print("Opción inválida")
        except (ValueError, OSError) as error:
            print("No se completó la operación:", error)
        except (EOFError, KeyboardInterrupt):
            print("\nSesión interrumpida; los cambios posteriores al último guardado se pierden")
            break


if __name__ == "__main__":
    main()
