# 10 · Pruebas y diseño mantenible

**Pregunta:** ¿Cómo demostrar que un cambio no rompió una regla anterior?

**Meta observable:** Probar comportamiento observable y separar dominio, interacción y almacenamiento.

**Sesiones 31–33:** tres encuentros de 120 minutos, adaptables. Prerrequisito: evidencias del módulo anterior.

## Conceptos con sentido

Una prueba automatizada prepara un caso, ejecuta una operación y verifica un resultado. Debe comprobar una regla significativa, no copiar el algoritmo. Un caso normal, uno límite y uno inválido ayudan a explorar el contrato, aunque pasar pruebas nunca demuestra ausencia total de errores.

Refactorizar cambia la organización conservando el comportamiento. La cohesión agrupa tareas relacionadas y el acoplamiento describe dependencias. Separar interfaz y dominio permite probar sin teclado. Introducimos responsabilidad única con ejemplos concretos; no hace falta crear una clase por cada función.

## Ruta de tres sesiones

| Sesión | Desarrollo | Evidencia |
|---|---|---|
| 31 · Comprender | 15 min problema; 25 actividad sin equipo; 25 explicación; 35 predicción y ejecución del ejemplo; 20 discusión | Descomposición y tabla de seguimiento |
| 32 · Modificar | 15 recuperación; 20 revisión del error frecuente; 60 taller niveles 1 y 2; 25 pruebas y explicación entre pares | Código modificado y casos de prueba |
| 33 · Transferir | 15 planeación; 60 reto nivel 3; 25 demostración individual; 20 retroalimentación | Solución propia, justificación y salida individual |

## Antes de ejecutar

Predice qué prueba falla si se elimina la validación de monto negativo. ¿Por qué probar solo 10 - 3 no detecta ese cambio?

Lee [el ejemplo](ejemplo.py), escribe tu predicción y después ejecuta desde la raíz:

```bash
python modulos/10_pruebas_y_diseno_mantenible/ejemplo.py
```

Salida esperada:

```text
El ejecutor de unittest informa 2 pruebas satisfactorias (OK); el tiempo puede variar.
```

En los primeros ejemplos aparecen funciones y validaciones que se profundizan después. Inicialmente sigue sus entradas y salidas; no se exige memorizar su sintaxis.

## Error para discutir

Probar solo que se creó un objeto no demuestra que proteja sus invariantes.

## Materiales y criterio de avance

- [Taller en tres niveles](taller.md).
- [Actividad sin computador](sin_computador.md).
- [Comprobación individual](evaluacion.md).
- [Orientaciones docentes](../../docente/solucionarios/10_pruebas_y_diseno_mantenible.md): contienen respuestas; consultar después del intento.

**Avanza cuando:** Cada prueba corresponde a una regla identificable; una refactorización conserva resultados y errores esperados. Si no se cumple, repite un caso pequeño con tabla de seguimiento y presenta una explicación nueva.

[Anterior](../09_archivos_y_persistencia/README.md) · [Ruta general](../../README.md) · [Siguiente](../11_proyecto_integrador_y_sustentacion/README.md)
