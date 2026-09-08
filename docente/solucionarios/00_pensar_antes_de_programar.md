# Orientación docente · Pensar antes de programar

Este repositorio es público: esta carpeta organiza las respuestas, no las oculta. Use variantes y defensa individual para valorar aprendizaje.

## Respuesta y justificación esperadas

Para grupos de máximo tres: (estudiantes + 2) // 3, con estudiantes enteros no negativos. Casos: 0→0, 1→1, 3→1, 4→2, 40→14. Se acepta otro algoritmo equivalente explicado. Si equipos_necesarios > disponibles debe reportarse que no alcanza la capacidad.

## Lectura del ejemplo

Resultado de referencia:

```text
0 estudiantes -> 0 equipos
1 estudiantes -> 1 equipos
2 estudiantes -> 1 equipos
5 estudiantes -> 3 equipos
40 estudiantes -> 20 equipos
```

Pida señalar el estado o expresión que produce cada resultado. En el módulo de pruebas, pida explicar qué conducta comprueba cada caso.

## Retroalimentación específica

Usar solamente estudiantes // 2 descarta al estudiante que queda sin pareja.

Ante este error, use el caso más pequeño que lo muestre y pida al estudiante explicar la diferencia entre su predicción y el resultado. No corrija solo la línea sin revisar el razonamiento.

## Aceptación de alternativas

Distingue cantidad de estudiantes de cantidad de equipos y justifica el redondeo hacia arriba con un caso impar. Acepte diseños distintos si cumplen el contrato y sus pruebas; no exija reproducir literalmente el ejemplo.

Para el reto abierto no existe una única solución: exija reglas explícitas, una decisión justificada y pruebas reproducibles. Aplique [la rúbrica común](../rubrica.md).
