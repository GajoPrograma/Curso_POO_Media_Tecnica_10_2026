# Comprobación individual

Duración: 15–25 minutos. Puede hacerse con papel. No consultar el solucionario durante el primer intento.

1. **Predicción (2 puntos).** Predice qué cambia si el archivo contiene una lista, un diccionario válido o un diccionario con cantidad -1.
2. **Explicación (2 puntos).** Explica con un caso concreto este error: Confiar en json.load como si validara las reglas del negocio permite cantidades negativas.
3. **Aplicación (4 puntos).** Prueba archivo ausente, JSON truncado y cantidad negativa. Registra la excepción de cada caso y el mensaje que mostrarías.
4. **Transferencia (2 puntos).** Propón un cambio de regla de esta situación y explica qué parte del modelo o programa habría que modificar.

Para la predicción y explicación: 0 sin evidencia; 1 parcialmente correcta; 2 correcta y justificada. Para aplicación: 0 sin propuesta; 1 idea sin completar; 2 resuelve caso normal; 3 incluye límite; 4 incluye inválido y justifica. Transferencia: 0 sin relación; 1 cambio pertinente sin impacto preciso; 2 cambio e impacto correctos.

**Criterio de avance sugerido:** 7/10 y evidencia de comprensión del criterio: Valida el esquema y no reemplaza silenciosamente datos dañados por un inventario vacío. No constituye una escala institucional oficial. Si hace falta apoyo, realiza una simulación pequeña y una nueva comprobación con datos diferentes.
