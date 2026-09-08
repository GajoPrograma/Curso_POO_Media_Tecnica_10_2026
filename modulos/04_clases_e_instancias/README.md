# 04 · Clases, instancias y métodos

**Pregunta:** ¿Cómo representar dos libros que cambian de estado de manera independiente?

**Meta observable:** Construir objetos con __init__, usar self y distinguir atributos de instancia.

**Sesiones 13–15:** tres encuentros de 120 minutos, adaptables. Prerrequisito: evidencias del módulo anterior.

## Conceptos con sentido

class define una clase. __init__ inicializa una instancia recién creada. self identifica la instancia que recibe una llamada; no representa a todas las instancias. Un método es una función asociada a una clase. Los atributos que asignamos con self pertenecen a cada instancia.

Libro("L1", "Robótica") y Libro("L2", "Robótica") crean instancias distintas. Si ambas variables apuntan a la misma instancia, un cambio será visible desde las dos referencias. Una lista definida como atributo de clase puede quedar compartida accidentalmente: las colecciones propias de cada objeto se inicializan en __init__.

## Ruta de tres sesiones

| Sesión | Desarrollo | Evidencia |
|---|---|---|
| 13 · Comprender | 15 min problema; 25 actividad sin equipo; 25 explicación; 35 predicción y ejecución del ejemplo; 20 discusión | Descomposición y tabla de seguimiento |
| 14 · Modificar | 15 recuperación; 20 revisión del error frecuente; 60 taller niveles 1 y 2; 25 pruebas y explicación entre pares | Código modificado y casos de prueba |
| 15 · Transferir | 15 planeación; 60 reto nivel 3; 25 demostración individual; 20 retroalimentación | Solución propia, justificación y salida individual |

## Antes de ejecutar

Predice la disponibilidad de a y b después de a.prestar(). Luego imagina c = a: ¿qué observa c?

Lee [el ejemplo](ejemplo.py), escribe tu predicción y después ejecuta desde la raíz:

```bash
python modulos/04_clases_e_instancias/ejemplo.py
```

Salida esperada:

```text
A disponible: False
B disponible: True
```

En los primeros ejemplos aparecen funciones y validaciones que se profundizan después. Inicialmente sigue sus entradas y salidas; no se exige memorizar su sintaxis.

## Error para discutir

Olvidar self crea una variable local que no actualiza el objeto.

## Materiales y criterio de avance

- [Taller en tres niveles](taller.md).
- [Actividad sin computador](sin_computador.md).
- [Comprobación individual](evaluacion.md).
- [Orientaciones docentes](../../docente/solucionarios/04_clases_e_instancias.md): contienen respuestas; consultar después del intento.

**Avanza cuando:** Explica self usando una instancia concreta y demuestra independencia entre objetos. Si no se cumple, repite un caso pequeño con tabla de seguimiento y presenta una explicación nueva.

[Anterior](../03_modelar_objetos/README.md) · [Ruta general](../../README.md) · [Siguiente](../05_encapsulacion_y_contratos/README.md)
