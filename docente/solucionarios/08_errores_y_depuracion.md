# Orientación docente · Errores, excepciones y depuración

Este repositorio es público: esta carpeta organiza las respuestas, no las oculta. Use variantes y defensa individual para valorar aprendizaje.

## Respuesta y justificación esperadas

"0" se convierte pero viola positividad; "hola" y "2.5" no se convierten con int. dividir(0, 2) debe retornar 0; dividir(2, 0) puede lanzar ZeroDivisionError y la interfaz lo comunica. Un error de límite se demuestra con el valor exacto del extremo, no solo con un valor interior.

## Lectura del ejemplo

Resultado de referencia:

```text
3
La cantidad debe ser positiva
Escribe un número entero
Escribe un número entero
```

Pida señalar el estado o expresión que produce cada resultado. En el módulo de pruebas, pida explicar qué conducta comprueba cada caso.

## Retroalimentación específica

Usar except: pass hace desaparecer el síntoma y puede simular que una operación sí ocurrió.

Ante este error, use el caso más pequeño que lo muestre y pida al estudiante explicar la diferencia entre su predicción y el resultado. No corrija solo la línea sin revisar el razonamiento.

## Aceptación de alternativas

Captura excepciones específicas y aporta un caso reproducible que demuestra la corrección. Acepte diseños distintos si cumplen el contrato y sus pruebas; no exija reproducir literalmente el ejemplo.

Para el reto abierto no existe una única solución: exija reglas explícitas, una decisión justificada y pruebas reproducibles. Aplique [la rúbrica común](../rubrica.md).
