# Orientación docente · Pruebas y diseño mantenible

Este repositorio es público: esta carpeta organiza las respuestas, no las oculta. Use variantes y defensa individual para valorar aprendizaje.

## Respuesta y justificación esperadas

Cuenta(5).retirar(5) deja 0. Un retiro 6 desde 5 genera ValueError y conserva 5. Dos cuentas nuevas no comparten saldo. Las pruebas del dominio no deben necesitar input ni archivos reales; los casos de persistencia usan carpetas temporales.

## Lectura del ejemplo

Resultado de referencia:

```text
El ejecutor de unittest informa 2 pruebas satisfactorias (OK); el tiempo puede variar.
```

Pida señalar el estado o expresión que produce cada resultado. En el módulo de pruebas, pida explicar qué conducta comprueba cada caso.

## Retroalimentación específica

Probar solo que se creó un objeto no demuestra que proteja sus invariantes.

Ante este error, use el caso más pequeño que lo muestre y pida al estudiante explicar la diferencia entre su predicción y el resultado. No corrija solo la línea sin revisar el razonamiento.

## Aceptación de alternativas

Cada prueba corresponde a una regla identificable; una refactorización conserva resultados y errores esperados. Acepte diseños distintos si cumplen el contrato y sus pruebas; no exija reproducir literalmente el ejemplo.

Para el reto abierto no existe una única solución: exija reglas explícitas, una decisión justificada y pruebas reproducibles. Aplique [la rúbrica común](../rubrica.md).
