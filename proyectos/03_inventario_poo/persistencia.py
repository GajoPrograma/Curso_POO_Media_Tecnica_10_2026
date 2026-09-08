"""JSON local: valida completamente antes de sustituir el inventario."""
import json
from pathlib import Path
import tempfile

from dominio import Inventario


def guardar(inventario, ruta):
    ruta = Path(ruta)
    ruta.parent.mkdir(parents=True, exist_ok=True)
    temporal = None
    try:
        with tempfile.NamedTemporaryFile(mode="w", encoding="utf-8",
                                         dir=ruta.parent, delete=False,
                                         prefix="inventario_", suffix=".tmp") as archivo:
            temporal = Path(archivo.name)
            json.dump(inventario.listar(), archivo, ensure_ascii=False, indent=2)
        temporal.replace(ruta)
    finally:
        if temporal is not None and temporal.exists():
            temporal.unlink()


def cargar(ruta):
    with open(ruta, encoding="utf-8") as archivo:
        datos = json.load(archivo)
    return Inventario.desde_datos(datos)
