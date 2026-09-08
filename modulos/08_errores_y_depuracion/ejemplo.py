def leer_cantidad(texto):
    try:
        cantidad = int(texto)
    except ValueError as error:
        raise ValueError("Escribe un número entero") from error
    if cantidad <= 0:
        raise ValueError("La cantidad debe ser positiva")
    return cantidad


if __name__ == "__main__":
    for entrada in ["3", "0", "hola", "2.5"]:
        try:
            print(leer_cantidad(entrada))
        except ValueError as error:
            print(error)
