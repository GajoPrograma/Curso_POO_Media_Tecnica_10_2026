# Orientación docente · Composición y colaboración

Este repositorio es público: esta carpeta organiza las respuestas, no las oculta. Use variantes y defensa individual para valorar aprendizaje.

## Respuesta y justificación esperadas

Biblioteca.devolver localiza el libro o genera ValueError y llama libro.devolver(). disponibles puede retornar una nueva lista de códigos. Equipo tiene componentes, pero no es un componente en el modelo propuesto; si otro modelo usa equipos anidados debe justificar el contrato compartido.

## Lectura del ejemplo

Resultado de referencia:

```text
Préstamo registrado
Libro ya prestado
```

Pida señalar el estado o expresión que produce cada resultado. En el módulo de pruebas, pida explicar qué conducta comprueba cada caso.

## Retroalimentación específica

Copiar la regla de disponibilidad en Biblioteca y Libro crea dos lugares que pueden contradecirse.

Ante este error, use el caso más pequeño que lo muestre y pida al estudiante explicar la diferencia entre su predicción y el resultado. No corrija solo la línea sin revisar el razonamiento.

## Aceptación de alternativas

La biblioteca delega la regla de préstamo; no modifica directamente atributos internos de Libro. Acepte diseños distintos si cumplen el contrato y sus pruebas; no exija reproducir literalmente el ejemplo.

Para el reto abierto no existe una única solución: exija reglas explícitas, una decisión justificada y pruebas reproducibles. Aplique [la rúbrica común](../rubrica.md).
