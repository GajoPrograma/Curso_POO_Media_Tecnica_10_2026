# 01 · Datos, decisiones y ciclos

**Pregunta:** ¿Cómo contar inscripciones válidas para un taller escolar?

**Meta observable:** Representar datos, construir condiciones y explicar la terminación de un ciclo.

**Sesiones 4–6:** tres encuentros de 120 minutos, adaptables. Prerrequisito: evidencias del módulo anterior.

## Conceptos con sentido

Una variable vincula un nombre con un valor. Los tipos básicos que usaremos son int, float, str y bool. Una comparación produce un booleano. if selecciona una ruta; for recorre una secuencia. input siempre devuelve texto: convertirlo exige considerar entradas inválidas.

Una condición debe traducir exactamente una regla. Si el taller permite edades entre 14 y 18 inclusive, ambos extremos cuentan. Un acumulador conserva un resultado parcial. En un for sobre una lista finita, el recorrido termina al agotar sus elementos; un while necesita una condición de salida que pueda alcanzarse.

## Ruta de tres sesiones

| Sesión | Desarrollo | Evidencia |
|---|---|---|
| 4 · Comprender | 15 min problema; 25 actividad sin equipo; 25 explicación; 35 predicción y ejecución del ejemplo; 20 discusión | Descomposición y tabla de seguimiento |
| 5 · Modificar | 15 recuperación; 20 revisión del error frecuente; 60 taller niveles 1 y 2; 25 pruebas y explicación entre pares | Código modificado y casos de prueba |
| 6 · Transferir | 15 planeación; 60 reto nivel 3; 25 demostración individual; 20 retroalimentación | Solución propia, justificación y salida individual |

## Antes de ejecutar

Sigue el valor de aceptados después de cada edad en [13, 14, 16, 18, 19]. No ejecutes hasta tener las cinco filas.

Lee [el ejemplo](ejemplo.py), escribe tu predicción y después ejecuta desde la raíz:

```bash
python modulos/01_datos_decisiones_y_ciclos/ejemplo.py
```

Salida esperada:

```text
Aceptados: 3
```

En los primeros ejemplos aparecen funciones y validaciones que se profundizan después. Inicialmente sigue sus entradas y salidas; no se exige memorizar su sintaxis.

## Error para discutir

Confundir < con <= excluye un extremo válido; reiniciar el contador dentro del ciclo borra el avance.

## Materiales y criterio de avance

- [Taller en tres niveles](taller.md).
- [Actividad sin computador](sin_computador.md).
- [Comprobación individual](evaluacion.md).
- [Orientaciones docentes](../../docente/solucionarios/01_datos_decisiones_y_ciclos.md): contienen respuestas; consultar después del intento.

**Avanza cuando:** Prueba ambos límites de edad y distingue rechazo por edad de rechazo por cupo. Si no se cumple, repite un caso pequeño con tabla de seguimiento y presenta una explicación nueva.

[Anterior](../00_pensar_antes_de_programar/README.md) · [Ruta general](../../README.md) · [Siguiente](../02_colecciones_funciones_y_modulos/README.md)
