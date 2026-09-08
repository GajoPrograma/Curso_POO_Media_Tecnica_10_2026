# Curso de Programación Orientada a Objetos · Media Técnica 10° · 2026

Curso en español para aprender a **descomponer problemas, representar reglas, construir soluciones y justificarlas**. Lenguaje de esta primera versión: Python. Docente: José Francisco Saavedra Díaz. Versión 1.0.0, 8 de septiembre de 2026.

## Empieza aquí

1. Docente: lee la [guía de implementación](docente/guia.md) y aplica el [diagnóstico](docente/diagnostico.md).
2. Estudiante: sigue la [instalación](estudiantes/instalacion.md) y la [forma de trabajar](estudiantes/como_trabajar.md).
3. Comienza por [pensar antes de programar](modulos/00_pensar_antes_de_programar/README.md).
4. Consulta el [mapa de sesiones](PLAN_CURRICULAR.md), la [rúbrica](docente/rubrica.md) y el [glosario](recursos/glosario.md).

## Ruta completa

36 sesiones de 120 minutos = **72 horas propuestas**, sin fechas fijas. No presupone que quepan en lo restante de 2026. Se ajusta al diagnóstico y al horario real; con encuentros de otra duración, redistribuye los bloques conservando evidencias y práctica.

| Módulo | Tema | Sesiones |
|---|---|---|
| 00 | [Pensar antes de programar](modulos/00_pensar_antes_de_programar/README.md) | 1–3 |
| 01 | [Datos, decisiones y ciclos](modulos/01_datos_decisiones_y_ciclos/README.md) | 4–6 |
| 02 | [Colecciones, funciones y módulos](modulos/02_colecciones_funciones_y_modulos/README.md) | 7–9 |
| 03 | [Modelar objetos y responsabilidades](modulos/03_modelar_objetos/README.md) | 10–12 |
| 04 | [Clases, instancias y métodos](modulos/04_clases_e_instancias/README.md) | 13–15 |
| 05 | [Encapsulación, propiedades y contratos](modulos/05_encapsulacion_y_contratos/README.md) | 16–18 |
| 06 | [Composición y colaboración](modulos/06_composicion_y_colaboracion/README.md) | 19–21 |
| 07 | [Herencia, polimorfismo y abstracción](modulos/07_herencia_polimorfismo_y_abstraccion/README.md) | 22–24 |
| 08 | [Errores, excepciones y depuración](modulos/08_errores_y_depuracion/README.md) | 25–27 |
| 09 | [Archivos JSON y persistencia](modulos/09_archivos_y_persistencia/README.md) | 28–30 |
| 10 | [Pruebas y diseño mantenible](modulos/10_pruebas_y_diseno_mantenible/README.md) | 31–33 |
| 11 | [Proyecto integrador y sustentación](modulos/11_proyecto_integrador_y_sustentacion/README.md) | 34–36 |

Cada módulo incluye explicación conceptual, ejemplo ejecutable, salida esperada, taller en tres niveles, actividad sin computador y evaluación individual. Las orientaciones docentes están separadas, pero son visibles en este repositorio público.

## Proyectos progresivos

- [01 · Calculadora robusta](proyectos/01_calculadora/README.md): funciones, contratos y errores; después del módulo 02, ampliable en 08.
- [02 · Biblioteca del aula](proyectos/02_biblioteca/README.md): objetos, estados y colaboración; módulos 03–06.
- [03 · Inventario de materiales](proyectos/03_inventario_poo/README.md): dominio, interfaz, JSON y pruebas; se diseña desde 05 y se integra en 09–11.

Los proyectos incluyen implementaciones de referencia funcionales. Los talleres piden extensiones para evitar que ejecutar el código se confunda con aprender. Las actividades de proyecto se integran en los bloques de práctica de las sesiones; no se suman 72 horas adicionales.

## Ejecutar y verificar

Python 3.10 o superior; solo biblioteca estándar, sin instalar paquetes externos. Desde la raíz:

```bash
python herramientas/verificar_curso.py
python -m unittest discover -s tests -v
python proyectos/03_inventario_poo/main.py
```

La verificación ejecuta ejemplos y pruebas con datos ficticios. El proyecto final es una aplicación de consola individual; no es un sistema multiusuario ni de producción.

## Mantener el curso en el tiempo

[Estado actual](ESTADO_CURSO.md) · [Cambios](CHANGELOG.md) · [Cómo contribuir](CONTRIBUTING.md) · [Próximas mejoras](ROADMAP.md) · [Plantilla de sesión](plantillas/sesion.md)

Después de cada clase registre dificultades observadas y cambios propuestos sin nombres ni información personal. Los commits conservan la historia; use ramas para preparar cambios y una revisión docente antes de darlos por material de aula.
