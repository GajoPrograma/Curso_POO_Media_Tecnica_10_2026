"""Pruebas de contratos: normales, límites, rechazo y persistencia."""
import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]


def modulo(nombre, ruta):
    spec = importlib.util.spec_from_file_location(nombre, ROOT / ruta)
    objeto = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(objeto)
    return objeto


calculadora = modulo("calculadora", "proyectos/01_calculadora/operaciones.py")
biblioteca = modulo("biblioteca", "proyectos/02_biblioteca/dominio.py")
inventario = modulo("inventario", "proyectos/03_inventario_poo/dominio.py")
# Los proyectos se ejecutan por separado. Se resuelve explícitamente el import
# local de persistencia para evitar confundir los archivos llamados dominio.py.
with patch.dict(sys.modules, {"dominio": inventario}):
    persistencia = modulo("persistencia_inventario", "proyectos/03_inventario_poo/persistencia.py")


class PruebasCalculadora(unittest.TestCase):
    def test_operaciones(self):
        for a, op, b, esperado in [(2,"+",3,5), (5,"-",2,3), (3,"*",4,12), (5,"/",2,2.5), (0,"/",5,0)]:
            with self.subTest(op=op, a=a):
                self.assertEqual(calculadora.calcular(a, op, b), esperado)

    def test_division_por_cero(self):
        with self.assertRaises(ZeroDivisionError):
            calculadora.calcular(5, "/", 0)

    def test_operador_invalido(self):
        with self.assertRaises(ValueError):
            calculadora.calcular(5, "^", 2)

    def test_operandos_invalidos(self):
        for dato in (True, "2", float("nan"), float("inf")):
            with self.subTest(dato=dato), self.assertRaises(ValueError):
                calculadora.calcular(dato, "+", 2)

    def test_resultado_no_finito(self):
        with self.assertRaises(ValueError):
            calculadora.calcular(1e308, "*", 1e308)


class PruebasBiblioteca(unittest.TestCase):
    def setUp(self):
        self.b = biblioteca.Biblioteca()
        self.b.agregar(biblioteca.Libro("L1", "Robótica"))
        self.b.agregar(biblioteca.Libro("L2", "Robótica"))

    def test_independencia_y_devolucion(self):
        self.b.prestar("L1")
        self.assertEqual([fila[2] for fila in self.b.catalogo()], [False, True])
        self.b.devolver("L1")
        self.assertTrue(self.b.catalogo()[0][2])

    def test_doble_prestamo_conserva_estado(self):
        self.b.prestar("L1")
        with self.assertRaises(ValueError):
            self.b.prestar("L1")
        self.assertFalse(self.b.catalogo()[0][2])

    def test_devolucion_invalida(self):
        with self.assertRaises(ValueError):
            self.b.devolver("L1")
        self.assertTrue(self.b.catalogo()[0][2])

    def test_duplicado_no_reemplaza(self):
        with self.assertRaises(ValueError):
            self.b.agregar(biblioteca.Libro("L1", "Otro"))
        self.assertEqual(self.b.catalogo()[0][1], "Robótica")

    def test_ausente(self):
        anterior = self.b.catalogo()
        with self.assertRaises(ValueError):
            self.b.prestar("X")
        self.assertEqual(self.b.catalogo(), anterior)

    def test_atributos_invalidos(self):
        for codigo, titulo in [("", "A"), ("A", "  "), (None, "A")]:
            with self.subTest(codigo=codigo), self.assertRaises(ValueError):
                biblioteca.Libro(codigo, titulo)


class PruebasInventario(unittest.TestCase):
    def setUp(self):
        self.inv = inventario.Inventario()
        self.inv.agregar("M1", "Relé", 5)

    def test_ingreso_y_retiro_exacto(self):
        self.inv.ingresar("M1", 2)
        self.inv.retirar("M1", 7)
        self.assertEqual(self.inv.listar()[0]["cantidad"], 0)

    def test_retiros_invalidos_conservan_estado(self):
        for cantidad in (6, 0, -1, True, 2.5, "2"):
            with self.subTest(cantidad=cantidad):
                with self.assertRaises(ValueError):
                    self.inv.retirar("M1", cantidad)
                self.assertEqual(self.inv.listar()[0]["cantidad"], 5)

    def test_ingresos_invalidos_conservan_estado(self):
        for cantidad in (0, -1, True, 2.5):
            with self.subTest(cantidad=cantidad), self.assertRaises(ValueError):
                self.inv.ingresar("M1", cantidad)
        self.assertEqual(self.inv.listar()[0]["cantidad"], 5)

    def test_cantidad_inicial_y_textos(self):
        self.inv.agregar("M0", "Cable", 0)
        for cantidad in (-1, True, 2.5):
            with self.subTest(cantidad=cantidad), self.assertRaises(ValueError):
                self.inv.agregar("M2", "Cable", cantidad)
        for codigo, nombre in [("", "A"), ("A", " "), (None, "A")]:
            with self.subTest(codigo=codigo), self.assertRaises(ValueError):
                self.inv.agregar(codigo, nombre)

    def test_duplicado_y_ausente(self):
        with self.assertRaises(ValueError):
            self.inv.agregar(" M1 ", "Otro", 8)
        with self.assertRaises(ValueError):
            self.inv.retirar("AUSENTE", 1)
        self.assertEqual(self.inv.listar(), [{"codigo":"M1", "nombre":"Relé", "cantidad":5}])

    def test_consulta_es_copia(self):
        consulta = self.inv.listar()
        consulta[0]["cantidad"] = -9
        consulta.clear()
        self.assertEqual(self.inv.listar()[0]["cantidad"], 5)

    def test_guardar_cargar_y_reemplazar(self):
        with tempfile.TemporaryDirectory() as carpeta:
            ruta = Path(carpeta) / "datos.json"
            persistencia.guardar(self.inv, ruta)
            recuperado = persistencia.cargar(ruta)
            self.assertEqual(recuperado.listar(), self.inv.listar())
            self.inv.retirar("M1", 2)
            persistencia.guardar(self.inv, ruta)
            self.assertEqual(persistencia.cargar(ruta).listar()[0]["cantidad"], 3)

    def test_archivo_ausente(self):
        with tempfile.TemporaryDirectory() as carpeta:
            with self.assertRaises(FileNotFoundError):
                persistencia.cargar(Path(carpeta) / "ausente.json")

    def test_json_danado_y_esquema_invalido(self):
        casos = ["{", "{}", '[{"codigo":"M1","nombre":"A","cantidad":-1}]',
                 '[{"codigo":"M1","nombre":"A","cantidad":true}]',
                 '[{"codigo":"M1"}]']
        with tempfile.TemporaryDirectory() as carpeta:
            ruta = Path(carpeta) / "datos.json"
            for contenido in casos:
                with self.subTest(contenido=contenido):
                    ruta.write_text(contenido, encoding="utf-8")
                    with self.assertRaises(ValueError):
                        persistencia.cargar(ruta)
                    self.assertEqual(ruta.read_text(encoding="utf-8"), contenido)

    def test_reconstruccion_rechaza_duplicados(self):
        datos = self.inv.listar() * 2
        with self.assertRaises(ValueError):
            inventario.Inventario.desde_datos(datos)

    def test_fallo_de_reemplazo_preserva_archivo(self):
        with tempfile.TemporaryDirectory() as carpeta:
            ruta = Path(carpeta) / "datos.json"
            persistencia.guardar(self.inv, ruta)
            original = ruta.read_bytes()
            self.inv.retirar("M1", 1)
            with patch.object(Path, "replace", side_effect=OSError("fallo simulado")):
                with self.assertRaises(OSError):
                    persistencia.guardar(self.inv, ruta)
            self.assertEqual(ruta.read_bytes(), original)
            self.assertEqual(list(Path(carpeta).glob("*.tmp")), [])


class PruebasConsola(unittest.TestCase):
    def test_calculadora_se_recupera(self):
        resultado = subprocess.run([sys.executable, str(ROOT / "proyectos/01_calculadora/main.py")],
                                   input="/\n5\n0\n+\n2\n3\nsalir\n", text=True,
                                   capture_output=True, timeout=10)
        self.assertEqual(resultado.returncode, 0, resultado.stderr)
        self.assertIn("No se puede dividir por cero", resultado.stdout)
        self.assertIn("Resultado: 5.0", resultado.stdout)


if __name__ == "__main__":
    unittest.main()
