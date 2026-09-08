# Orientación docente · Encapsulación, propiedades y contratos

Este repositorio es público: esta carpeta organiza las respuestas, no las oculta. Use variantes y defensa individual para valorar aprendizaje.

## Respuesta y justificación esperadas

ingresar debe comprobar type(cantidad) is int y cantidad > 0 antes de sumar. bool es subtipo de int en Python, por eso este contrato usa type exacto. Después de retirar 2 e intentar retirar 4, quedan 3 unidades. El uso de _ no impide acceso deliberado.

## Lectura del ejemplo

Resultado de referencia:

```text
Existencias insuficientes
Unidades: 3
```

Pida señalar el estado o expresión que produce cada resultado. En el módulo de pruebas, pida explicar qué conducta comprueba cada caso.

## Retroalimentación específica

Restar antes de validar deja el objeto corrupto aunque luego se lance una excepción.

Ante este error, use el caso más pequeño que lo muestre y pida al estudiante explicar la diferencia entre su predicción y el resultado. No corrija solo la línea sin revisar el razonamiento.

## Aceptación de alternativas

Las operaciones rechazadas conservan el estado; diferencia convención de privacidad de control de acceso. Acepte diseños distintos si cumplen el contrato y sus pruebas; no exija reproducir literalmente el ejemplo.

Para el reto abierto no existe una única solución: exija reglas explícitas, una decisión justificada y pruebas reproducibles. Aplique [la rúbrica común](../rubrica.md).
