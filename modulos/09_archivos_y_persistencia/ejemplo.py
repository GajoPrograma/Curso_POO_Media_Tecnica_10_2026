import json
from pathlib import Path
from tempfile import TemporaryDirectory


def validar(datos):
    if not isinstance(datos, dict):
        raise ValueError("Se esperaba un diccionario")
    for nombre, cantidad in datos.items():
        if not isinstance(nombre, str) or not nombre.strip():
            raise ValueError("Nombre inválido")
        if type(cantidad) is not int or cantidad < 0:
            raise ValueError("Cantidad inválida")
    return datos


def guardar(ruta, datos):
    validar(datos)
    with open(ruta, "w", encoding="utf-8") as archivo:
        json.dump(datos, archivo, ensure_ascii=False, indent=2)


def cargar(ruta):
    with open(ruta, encoding="utf-8") as archivo:
        return validar(json.load(archivo))


if __name__ == "__main__":
    with TemporaryDirectory() as carpeta:
        ruta = Path(carpeta) / "inventario.json"
        guardar(ruta, {"relé": 3})
        print(cargar(ruta))
