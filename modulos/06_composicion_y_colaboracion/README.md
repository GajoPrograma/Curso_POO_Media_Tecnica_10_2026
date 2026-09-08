# 06 · Composición y colaboración

**Pregunta:** ¿Cómo controla una biblioteca varios libros sin decidir por cada libro?

**Meta observable:** Construir un objeto con colaboradores y evitar duplicar responsabilidades.

**Sesiones 19–21:** tres encuentros de 120 minutos, adaptables. Prerrequisito: evidencias del módulo anterior.

## Conceptos con sentido

La composición permite construir un comportamiento usando otros objetos: una biblioteca contiene libros. Una relación de uso o pertenencia no implica herencia. En UML, la composición estricta implica propiedad del ciclo de vida; contener referencias en Python no garantiza por sí solo esa semántica.

Biblioteca busca por código; Libro decide si puede prestarse. La coordinación delega en quien conoce la regla. Usamos un diccionario interno para buscar por código y rechazamos códigos duplicados. Un diseño de objetos debe aclarar quién puede cambiar cada estado.

## Ruta de tres sesiones

| Sesión | Desarrollo | Evidencia |
|---|---|---|
| 19 · Comprender | 15 min problema; 25 actividad sin equipo; 25 explicación; 35 predicción y ejecución del ejemplo; 20 discusión | Descomposición y tabla de seguimiento |
| 20 · Modificar | 15 recuperación; 20 revisión del error frecuente; 60 taller niveles 1 y 2; 25 pruebas y explicación entre pares | Código modificado y casos de prueba |
| 21 · Transferir | 15 planeación; 60 reto nivel 3; 25 demostración individual; 20 retroalimentación | Solución propia, justificación y salida individual |

## Antes de ejecutar

Agrega L1 y solicita prestarlo dos veces. Señala qué objeto busca y cuál rechaza el segundo préstamo.

Lee [el ejemplo](ejemplo.py), escribe tu predicción y después ejecuta desde la raíz:

```bash
python modulos/06_composicion_y_colaboracion/ejemplo.py
```

Salida esperada:

```text
Préstamo registrado
Libro ya prestado
```

En los primeros ejemplos aparecen funciones y validaciones que se profundizan después. Inicialmente sigue sus entradas y salidas; no se exige memorizar su sintaxis.

## Error para discutir

Copiar la regla de disponibilidad en Biblioteca y Libro crea dos lugares que pueden contradecirse.

## Materiales y criterio de avance

- [Taller en tres niveles](taller.md).
- [Actividad sin computador](sin_computador.md).
- [Comprobación individual](evaluacion.md).
- [Orientaciones docentes](../../docente/solucionarios/06_composicion_y_colaboracion.md): contienen respuestas; consultar después del intento.

**Avanza cuando:** La biblioteca delega la regla de préstamo; no modifica directamente atributos internos de Libro. Si no se cumple, repite un caso pequeño con tabla de seguimiento y presenta una explicación nueva.

[Anterior](../05_encapsulacion_y_contratos/README.md) · [Ruta general](../../README.md) · [Siguiente](../07_herencia_polimorfismo_y_abstraccion/README.md)
