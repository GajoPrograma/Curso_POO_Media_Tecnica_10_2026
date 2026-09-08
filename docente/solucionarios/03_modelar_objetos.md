# Orientación docente · Modelar objetos y responsabilidades

Este repositorio es público: esta carpeta organiza las respuestas, no las oculta. Use variantes y defensa individual para valorar aprendizaje.

## Respuesta y justificación esperadas

Libro conoce su disponibilidad y valida prestar/devolver; Biblioteca localiza libros por código y coordina préstamos. Prestar un libro prestado y devolver uno disponible son transiciones rechazadas. Dos ejemplares del mismo título requieren códigos diferentes. El diccionario es simple, pero no protege las reglas de modificación.

## Lectura del ejemplo

Resultado de referencia:

```text
Primer préstamo: True
Segundo préstamo: False
```

Pida señalar el estado o expresión que produce cada resultado. En el módulo de pruebas, pida explicar qué conducta comprueba cada caso.

## Retroalimentación específica

Poner todas las operaciones en una clase Sistema produce una clase con demasiadas responsabilidades.

Ante este error, use el caso más pequeño que lo muestre y pida al estudiante explicar la diferencia entre su predicción y el resultado. No corrija solo la línea sin revisar el razonamiento.

## Aceptación de alternativas

Asigna responsabilidades con una razón y distingue identidad de igualdad de atributos. Acepte diseños distintos si cumplen el contrato y sus pruebas; no exija reproducir literalmente el ejemplo.

Para el reto abierto no existe una única solución: exija reglas explícitas, una decisión justificada y pruebas reproducibles. Aplique [la rúbrica común](../rubrica.md).
