# 03 · Modelar objetos y responsabilidades

**Pregunta:** ¿Qué necesita saber y hacer un libro del aula para ser prestado?

**Meta observable:** Identificar estado, comportamiento, identidad y reglas antes de escribir una clase.

**Sesiones 10–12:** tres encuentros de 120 minutos, adaptables. Prerrequisito: evidencias del módulo anterior.

## Conceptos con sentido

Un objeto reúne estado y comportamiento. Una clase define cómo construir objetos de un tipo. La identidad permite distinguir dos objetos con atributos iguales. No todo sustantivo debe convertirse en clase: conviene modelar entidades que tienen responsabilidades o reglas relevantes.

Una tarjeta CRC contiene clase, responsabilidades y colaboradores. El estado de un libro puede ser disponible o prestado, pero debe definirse qué operaciones cambian ese estado. Un modelo es una simplificación del problema: aún no necesitamos pantallas, bases de datos ni datos personales de estudiantes.

## Ruta de tres sesiones

| Sesión | Desarrollo | Evidencia |
|---|---|---|
| 10 · Comprender | 15 min problema; 25 actividad sin equipo; 25 explicación; 35 predicción y ejecución del ejemplo; 20 discusión | Descomposición y tabla de seguimiento |
| 11 · Modificar | 15 recuperación; 20 revisión del error frecuente; 60 taller niveles 1 y 2; 25 pruebas y explicación entre pares | Código modificado y casos de prueba |
| 12 · Transferir | 15 planeación; 60 reto nivel 3; 25 demostración individual; 20 retroalimentación | Solución propia, justificación y salida individual |

## Antes de ejecutar

En el ejemplo procedural, sigue disponible al prestar dos veces. Explica qué regla impide el segundo préstamo y qué ocurriría si cualquier parte del programa cambiara el diccionario.

Lee [el ejemplo](ejemplo.py), escribe tu predicción y después ejecuta desde la raíz:

```bash
python modulos/03_modelar_objetos/ejemplo.py
```

Salida esperada:

```text
Primer préstamo: True
Segundo préstamo: False
```

En los primeros ejemplos aparecen funciones y validaciones que se profundizan después. Inicialmente sigue sus entradas y salidas; no se exige memorizar su sintaxis.

## Error para discutir

Poner todas las operaciones en una clase Sistema produce una clase con demasiadas responsabilidades.

## Materiales y criterio de avance

- [Taller en tres niveles](taller.md).
- [Actividad sin computador](sin_computador.md).
- [Comprobación individual](evaluacion.md).
- [Orientaciones docentes](../../docente/solucionarios/03_modelar_objetos.md): contienen respuestas; consultar después del intento.

**Avanza cuando:** Asigna responsabilidades con una razón y distingue identidad de igualdad de atributos. Si no se cumple, repite un caso pequeño con tabla de seguimiento y presenta una explicación nueva.

[Anterior](../02_colecciones_funciones_y_modulos/README.md) · [Ruta general](../../README.md) · [Siguiente](../04_clases_e_instancias/README.md)
