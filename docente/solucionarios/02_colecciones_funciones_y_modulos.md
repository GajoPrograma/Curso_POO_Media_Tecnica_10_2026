# Orientación docente · Colecciones, funciones y módulos

Este repositorio es público: esta carpeta organiza las respuestas, no las oculta. Use variantes y defensa individual para valorar aprendizaje.

## Respuesta y justificación esperadas

unidades_de puede usar inventario.get(nombre, 0). El filtro puede usar {nombre: cantidad for nombre, cantidad in inventario.items() if cantidad > 0}. Probar {"led": 0, "cable": 3} produce {"cable": 3} y el original permanece igual. No se necesita una clase para sumar cantidades.

## Lectura del ejemplo

Resultado de referencia:

```text
Unidades: 7
Inventario vacío: 0
```

Pida señalar el estado o expresión que produce cada resultado. En el módulo de pruebas, pida explicar qué conducta comprueba cada caso.

## Retroalimentación específica

Retornar dentro de la primera iteración suma solo el primer material.

Ante este error, use el caso más pequeño que lo muestre y pida al estudiante explicar la diferencia entre su predicción y el resultado. No corrija solo la línea sin revisar el razonamiento.

## Aceptación de alternativas

Diferencia imprimir de retornar, contempla una colección vacía y comprueba que el filtro no modifica la entrada. Acepte diseños distintos si cumplen el contrato y sus pruebas; no exija reproducir literalmente el ejemplo.

Para el reto abierto no existe una única solución: exija reglas explícitas, una decisión justificada y pruebas reproducibles. Aplique [la rúbrica común](../rubrica.md).
