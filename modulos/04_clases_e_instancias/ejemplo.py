class Libro:
    def __init__(self, codigo, titulo):
        self.codigo = codigo
        self.titulo = titulo
        self.disponible = True

    def prestar(self):
        if not self.disponible:
            return False
        self.disponible = False
        return True


if __name__ == "__main__":
    a = Libro("L1", "Robótica")
    b = Libro("L2", "Robótica")
    a.prestar()
    print("A disponible:", a.disponible)
    print("B disponible:", b.disponible)
