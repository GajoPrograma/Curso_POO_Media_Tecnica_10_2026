"""Modelo de préstamos de ejemplares, sin personas ni almacenamiento."""


class Libro:
    def __init__(self, codigo, titulo):
        if not isinstance(codigo, str) or not codigo.strip():
            raise ValueError("Código vacío o inválido")
        if not isinstance(titulo, str) or not titulo.strip():
            raise ValueError("Título vacío o inválido")
        self._codigo = codigo.strip()
        self._titulo = titulo.strip()
        self._disponible = True

    @property
    def codigo(self):
        return self._codigo

    @property
    def titulo(self):
        return self._titulo

    @property
    def disponible(self):
        return self._disponible

    def prestar(self):
        if not self.disponible:
            raise ValueError("Libro ya prestado")
        self._disponible = False

    def devolver(self):
        if self.disponible:
            raise ValueError("Libro ya disponible")
        self._disponible = True


class Biblioteca:
    def __init__(self):
        self._libros = {}

    def agregar(self, libro):
        if not isinstance(libro, Libro):
            raise ValueError("Se esperaba un Libro")
        if libro.codigo in self._libros:
            raise ValueError("Código duplicado")
        self._libros[libro.codigo] = libro

    def _buscar(self, codigo):
        if codigo not in self._libros:
            raise ValueError("Libro inexistente")
        return self._libros[codigo]

    def prestar(self, codigo):
        self._buscar(codigo).prestar()

    def devolver(self, codigo):
        self._buscar(codigo).devolver()

    def catalogo(self):
        return [(libro.codigo, libro.titulo, libro.disponible)
                for libro in self._libros.values()]
