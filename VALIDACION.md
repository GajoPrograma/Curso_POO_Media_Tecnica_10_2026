# Verificación de la versión 1.0.0

Fecha: 2026-09-08. Entorno de comprobación: Python 3.12.13 sobre Linux. Se propone Python 3.10 o superior; no se ejecutó una matriz de versiones ni una prueba presencial en Windows.

- 12 ejemplos ejecutados correctamente; salidas contrastadas con las guías. El ejemplo de unittest ejecuta sus dos pruebas internas.
- 23 pruebas automatizadas de proyectos satisfactorias: operaciones, errores, estados de préstamo, invariantes, independencia de consultas, JSON y fallo simulado de reemplazo de archivo.
- Enlaces relativos de los documentos comprobados con herramientas/verificar_curso.py.
- Flujo de consola del inventario comprobado en carpeta temporal: agregar 5 unidades, retirar 2, guardar, reiniciar, recuperar 3 y rechazar retiro de 4 conservando 3.
- Archivo JSON dañado: el arranque informa el problema y conserva el archivo original.

Reproducir ejemplos, enlaces y pruebas:

```bash
python herramientas/verificar_curso.py
```

Estas verificaciones cubren comportamiento técnico seleccionado. No prueban efectividad pedagógica, suficiencia de los tiempos ni ausencia de todos los errores. Esos aspectos deben revisarse al implementar el curso.
