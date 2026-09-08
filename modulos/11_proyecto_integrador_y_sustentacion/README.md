# 11 · Proyecto integrador y sustentación

**Pregunta:** ¿Cómo sabemos que resolvimos una necesidad y que cada integrante comprende el sistema?

**Meta observable:** Entregar una solución comprobable, explicar decisiones y adaptarla a un requisito nuevo.

**Sesiones 34–36:** tres encuentros de 120 minutos, adaptables. Prerrequisito: evidencias del módulo anterior.

## Conceptos con sentido

Un producto mínimo aborda un conjunto pequeño y explícito de necesidades. Un criterio de aceptación describe una conducta observable. Una iteración agrega una mejora verificable. La trazabilidad relaciona requisito, decisión, implementación y prueba.

El cierre incluye demostración, casos inválidos, límites conocidos y defensa individual. La interfaz llamativa no compensa reglas equivocadas. La evidencia de aprendizaje incluye predicciones y explicaciones anteriores a la solución, además del programa final. No es obligatorio usar herencia en el proyecto si el dominio no la justifica.

## Ruta de tres sesiones

| Sesión | Desarrollo | Evidencia |
|---|---|---|
| 34 · Comprender | 15 min problema; 25 actividad sin equipo; 25 explicación; 35 predicción y ejecución del ejemplo; 20 discusión | Descomposición y tabla de seguimiento |
| 35 · Modificar | 15 recuperación; 20 revisión del error frecuente; 60 taller niveles 1 y 2; 25 pruebas y explicación entre pares | Código modificado y casos de prueba |
| 36 · Transferir | 15 planeación; 60 reto nivel 3; 25 demostración individual; 20 retroalimentación | Solución propia, justificación y salida individual |

## Antes de ejecutar

Clasifica REQ-01 y REQ-02 en el ejemplo; determina por qué todos sobre una lista vacía daría una señal engañosa sin el control adicional.

Lee [el ejemplo](ejemplo.py), escribe tu predicción y después ejecuta desde la raíz:

```bash
python modulos/11_proyecto_integrador_y_sustentacion/ejemplo.py
```

Salida esperada:

```text
Listo: False
Sin requisitos: False
```

En los primeros ejemplos aparecen funciones y validaciones que se profundizan después. Inicialmente sigue sus entradas y salidas; no se exige memorizar su sintaxis.

## Error para discutir

Marcar requisitos como cumplidos sin una evidencia reproducible confunde intención con verificación.

## Materiales y criterio de avance

- [Taller en tres niveles](taller.md).
- [Actividad sin computador](sin_computador.md).
- [Comprobación individual](evaluacion.md).
- [Orientaciones docentes](../../docente/solucionarios/11_proyecto_integrador_y_sustentacion.md): contienen respuestas; consultar después del intento.

**Avanza cuando:** Cada integrante explica una regla y realiza un cambio; la matriz vincula requisitos reales con evidencia ejecutable. Si no se cumple, repite un caso pequeño con tabla de seguimiento y presenta una explicación nueva.

[Anterior](../10_pruebas_y_diseno_mantenible/README.md) · [Ruta general](../../README.md) · [Siguiente](../../proyectos/03_inventario_poo/README.md)
