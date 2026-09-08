# 00 · Pensar antes de programar

**Pregunta:** ¿Cómo asignar computadores sin dejar estudiantes sin puesto?

**Meta observable:** Descomponer un problema, precisar reglas y seguir un algoritmo sin ejecutar código.

**Sesiones 1–3:** tres encuentros de 120 minutos, adaptables. Prerrequisito: diagnóstico inicial; no requiere programación previa.

## Conceptos con sentido

Un problema se describe con entradas, salidas y restricciones. Un algoritmo es una secuencia finita de pasos precisos. Descomponer significa separar decisiones pequeñas que se puedan comprobar. Una prueba de escritorio registra cómo cambia cada variable; no consiste en adivinar la salida.

Para repartir estudiantes en parejas, la división entera cuenta parejas completas y el residuo identifica a quien queda solo. Debemos precisar si se permite compartir equipo, qué ocurre si faltan equipos y si cero estudiantes es válido. Cambiar una restricción puede cambiar todo el algoritmo.

## Ruta de tres sesiones

| Sesión | Desarrollo | Evidencia |
|---|---|---|
| 1 · Comprender | 15 min problema; 25 actividad sin equipo; 25 explicación; 35 predicción y ejecución del ejemplo; 20 discusión | Descomposición y tabla de seguimiento |
| 2 · Modificar | 15 recuperación; 20 revisión del error frecuente; 60 taller niveles 1 y 2; 25 pruebas y explicación entre pares | Código modificado y casos de prueba |
| 3 · Transferir | 15 planeación; 60 reto nivel 3; 25 demostración individual; 20 retroalimentación | Solución propia, justificación y salida individual |

## Antes de ejecutar

Antes de ejecutar, completa para 0, 1, 2, 5 y 40 estudiantes: parejas completas, estudiantes sin pareja y equipos necesarios. Explica por qué 5 estudiantes necesitan 3 equipos.

Lee [el ejemplo](ejemplo.py), escribe tu predicción y después ejecuta desde la raíz:

```bash
python modulos/00_pensar_antes_de_programar/ejemplo.py
```

Salida esperada:

```text
0 estudiantes -> 0 equipos
1 estudiantes -> 1 equipos
2 estudiantes -> 1 equipos
5 estudiantes -> 3 equipos
40 estudiantes -> 20 equipos
```

En los primeros ejemplos aparecen funciones y validaciones que se profundizan después. Inicialmente sigue sus entradas y salidas; no se exige memorizar su sintaxis.

## Error para discutir

Usar solamente estudiantes // 2 descarta al estudiante que queda sin pareja.

## Materiales y criterio de avance

- [Taller en tres niveles](taller.md).
- [Actividad sin computador](sin_computador.md).
- [Comprobación individual](evaluacion.md).
- [Orientaciones docentes](../../docente/solucionarios/00_pensar_antes_de_programar.md): contienen respuestas; consultar después del intento.

**Avanza cuando:** Distingue cantidad de estudiantes de cantidad de equipos y justifica el redondeo hacia arriba con un caso impar. Si no se cumple, repite un caso pequeño con tabla de seguimiento y presenta una explicación nueva.

[Anterior](../../README.md) · [Ruta general](../../README.md) · [Siguiente](../01_datos_decisiones_y_ciclos/README.md)
