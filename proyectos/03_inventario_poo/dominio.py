"""Reglas del inventario. No conoce teclado ni archivos."""


def texto_no_vacio(valor, campo):
    if not isinstance(valor, str) or not valor.strip():
        raise ValueError(f"{campo} debe ser texto no vacío")
    return valor.strip()


def entero_no_negativo(valor):
    if type(valor) is not int or valor < 0:
        raise ValueError("La cantidad debe ser un entero no negativo")
    return valor


class Material:
    def __init__(self, codigo, nombre, cantidad=0):
        self._codigo = texto_no_vacio(codigo, "Código")
        self._nombre = texto_no_vacio(nombre, "Nombre")
        self._cantidad = entero_no_negativo(cantidad)

    @property
    def codigo(self):
        return self._codigo

    @property
    def nombre(self):
        return self._nombre

    @property
    def cantidad(self):
        return self._cantidad

    def ingresar(self, cantidad):
        self._validar_movimiento(cantidad)
        self._cantidad += cantidad

    def retirar(self, cantidad):
        self._validar_movimiento(cantidad)
        if cantidad > self.cantidad:
            raise ValueError("Existencias insuficientes")
        self._cantidad -= cantidad

    @staticmethod
    def _validar_movimiento(cantidad):
        entero_no_negativo(cantidad)
        if cantidad == 0:
            raise ValueError("El movimiento debe ser positivo")

    def a_datos(self):
        return {"codigo": self.codigo, "nombre": self.nombre,
                "cantidad": self.cantidad}


class Inventario:
    def __init__(self):
        self._materiales = {}

    def agregar(self, codigo, nombre, cantidad=0):
        material = Material(codigo, nombre, cantidad)
        if material.codigo in self._materiales:
            raise ValueError("Código duplicado")
        self._materiales[material.codigo] = material

    def _buscar(self, codigo):
        codigo = texto_no_vacio(codigo, "Código")
        if codigo not in self._materiales:
            raise ValueError("Material inexistente")
        return self._materiales[codigo]

    def ingresar(self, codigo, cantidad):
        self._buscar(codigo).ingresar(cantidad)

    def retirar(self, codigo, cantidad):
        self._buscar(codigo).retirar(cantidad)

    def listar(self):
        # Devuelve copias de datos; no expone los objetos internos.
        return [material.a_datos() for material in self._materiales.values()]

    @classmethod
    def desde_datos(cls, datos):
        if not isinstance(datos, list):
            raise ValueError("Se esperaba una lista de materiales")
        nuevo = cls()
        for fila in datos:
            if not isinstance(fila, dict) or set(fila) != {"codigo", "nombre", "cantidad"}:
                raise ValueError("Estructura de material inválida")
            nuevo.agregar(fila["codigo"], fila["nombre"], fila["cantidad"])
        return nuevo
