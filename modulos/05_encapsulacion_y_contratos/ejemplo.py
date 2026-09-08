class Material:
    def __init__(self, cantidad):
        if type(cantidad) is not int or cantidad < 0:
            raise ValueError("Cantidad inicial inválida")
        self._cantidad = cantidad

    @property
    def cantidad(self):
        return self._cantidad

    def retirar(self, cantidad):
        if type(cantidad) is not int or cantidad <= 0:
            raise ValueError("La solicitud debe ser un entero positivo")
        if cantidad > self._cantidad:
            raise ValueError("Existencias insuficientes")
        self._cantidad -= cantidad


if __name__ == "__main__":
    material = Material(5)
    material.retirar(2)
    try:
        material.retirar(4)
    except ValueError as error:
        print(error)
    print("Unidades:", material.cantidad)
