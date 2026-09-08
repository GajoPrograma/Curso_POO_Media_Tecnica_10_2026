class Libro:
    def __init__(self, codigo):
        self.codigo = codigo
        self.disponible = True

    def prestar(self):
        if not self.disponible:
            raise ValueError("Libro ya prestado")
        self.disponible = False


class Biblioteca:
    def __init__(self):
        self._libros = {}

    def agregar(self, libro):
        if libro.codigo in self._libros:
            raise ValueError("Código duplicado")
        self._libros[libro.codigo] = libro

    def prestar(self, codigo):
        if codigo not in self._libros:
            raise ValueError("Libro inexistente")
        self._libros[codigo].prestar()


if __name__ == "__main__":
    biblioteca = Biblioteca()
    biblioteca.agregar(Libro("L1"))
    biblioteca.prestar("L1")
    print("Préstamo registrado")
    try:
        biblioteca.prestar("L1")
    except ValueError as error:
        print(error)
