# Orientación docente · Archivos JSON y persistencia

Este repositorio es público: esta carpeta organiza las respuestas, no las oculta. Use variantes y defensa individual para valorar aprendizaje.

## Respuesta y justificación esperadas

Archivo ausente: FileNotFoundError; JSON truncado: json.JSONDecodeError; cantidad negativa: ValueError de validación. El reemplazo con Path.replace reduce el riesgo de dejar un archivo parcial si temporal y destino están en el mismo sistema de archivos; no sustituye copias de seguridad ni coordinación de varios escritores.

## Lectura del ejemplo

Resultado de referencia:

```text
{'relé': 3}
```

Pida señalar el estado o expresión que produce cada resultado. En el módulo de pruebas, pida explicar qué conducta comprueba cada caso.

## Retroalimentación específica

Confiar en json.load como si validara las reglas del negocio permite cantidades negativas.

Ante este error, use el caso más pequeño que lo muestre y pida al estudiante explicar la diferencia entre su predicción y el resultado. No corrija solo la línea sin revisar el razonamiento.

## Aceptación de alternativas

Valida el esquema y no reemplaza silenciosamente datos dañados por un inventario vacío. Acepte diseños distintos si cumplen el contrato y sus pruebas; no exija reproducir literalmente el ejemplo.

Para el reto abierto no existe una única solución: exija reglas explícitas, una decisión justificada y pruebas reproducibles. Aplique [la rúbrica común](../rubrica.md).
