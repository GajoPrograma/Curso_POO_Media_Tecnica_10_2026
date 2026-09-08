# Orientación docente · Herencia, polimorfismo y abstracción

Este repositorio es público: esta carpeta organiza las respuestas, no las oculta. Use variantes y defensa individual para valorar aprendizaje.

## Respuesta y justificación esperadas

NotificadorMayusculas.enviar retorna texto.upper(). El historial se inicializa con self.historial = [] dentro de __init__. Una implementación que siempre falla no satisface el contrato de confirmar mensajes válidos; es preferible un colaborador opcional o explicitar un contrato de fallos compartido.

## Lectura del ejemplo

Resultado de referencia:

```text
Pantalla: Devolver L1
Simulado: Devolver L1
```

Pida señalar el estado o expresión que produce cada resultado. En el módulo de pruebas, pida explicar qué conducta comprueba cada caso.

## Retroalimentación específica

Una jerarquía larga no implica un mejor modelo; si el subtipo rechaza todos los casos válidos no es sustituible.

Ante este error, use el caso más pequeño que lo muestre y pida al estudiante explicar la diferencia entre su predicción y el resultado. No corrija solo la línea sin revisar el razonamiento.

## Aceptación de alternativas

Añade una implementación sin condicionales por tipo y justifica sustitución con ejemplos. Acepte diseños distintos si cumplen el contrato y sus pruebas; no exija reproducir literalmente el ejemplo.

Para el reto abierto no existe una única solución: exija reglas explícitas, una decisión justificada y pruebas reproducibles. Aplique [la rúbrica común](../rubrica.md).
