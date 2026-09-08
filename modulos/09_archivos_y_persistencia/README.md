# 09 · Archivos JSON y persistencia

**Pregunta:** ¿Cómo conservar un inventario al cerrar el programa?

**Meta observable:** Guardar y recuperar datos, validando estructura y reglas antes de aceptarlos.

**Sesiones 28–30:** tres encuentros de 120 minutos, adaptables. Prerrequisito: evidencias del módulo anterior.

## Conceptos con sentido

Persistencia significa conservar datos más allá de una ejecución. JSON representa datos, no métodos de objetos. Serializar convierte nuestro estado a una estructura guardable; reconstruir requiere validar antes de crear los objetos. Un JSON sintácticamente válido aún puede contener datos inválidos.

with cierra el archivo incluso si ocurre un error. encoding="utf-8" conserva texto en español. No confundir un archivo ausente con uno dañado: iniciar vacío puede ser una decisión válida para el primero, pero ocultar el segundo puede ocasionar pérdida de información. El ejemplo usa un directorio temporal que se elimina al terminar.

## Ruta de tres sesiones

| Sesión | Desarrollo | Evidencia |
|---|---|---|
| 28 · Comprender | 15 min problema; 25 actividad sin equipo; 25 explicación; 35 predicción y ejecución del ejemplo; 20 discusión | Descomposición y tabla de seguimiento |
| 29 · Modificar | 15 recuperación; 20 revisión del error frecuente; 60 taller niveles 1 y 2; 25 pruebas y explicación entre pares | Código modificado y casos de prueba |
| 30 · Transferir | 15 planeación; 60 reto nivel 3; 25 demostración individual; 20 retroalimentación | Solución propia, justificación y salida individual |

## Antes de ejecutar

Predice qué cambia si el archivo contiene una lista, un diccionario válido o un diccionario con cantidad -1.

Lee [el ejemplo](ejemplo.py), escribe tu predicción y después ejecuta desde la raíz:

```bash
python modulos/09_archivos_y_persistencia/ejemplo.py
```

Salida esperada:

```text
{'relé': 3}
```

En los primeros ejemplos aparecen funciones y validaciones que se profundizan después. Inicialmente sigue sus entradas y salidas; no se exige memorizar su sintaxis.

## Error para discutir

Confiar en json.load como si validara las reglas del negocio permite cantidades negativas.

## Materiales y criterio de avance

- [Taller en tres niveles](taller.md).
- [Actividad sin computador](sin_computador.md).
- [Comprobación individual](evaluacion.md).
- [Orientaciones docentes](../../docente/solucionarios/09_archivos_y_persistencia.md): contienen respuestas; consultar después del intento.

**Avanza cuando:** Valida el esquema y no reemplaza silenciosamente datos dañados por un inventario vacío. Si no se cumple, repite un caso pequeño con tabla de seguimiento y presenta una explicación nueva.

[Anterior](../08_errores_y_depuracion/README.md) · [Ruta general](../../README.md) · [Siguiente](../10_pruebas_y_diseno_mantenible/README.md)
