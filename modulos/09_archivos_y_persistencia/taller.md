# Taller · Archivos JSON y persistencia

Trabaja en pareja, pero cada integrante entrega su predicción y explicación. Cambien conductor y observador cada 15–20 minutos. En un trío, la tercera persona diseña pruebas y rota también.

## 1. Comprender

Añade dos materiales y verifica que guardar y cargar conserva nombres y cantidades, incluidas tildes.

Antes de escribir código: identifica entradas, salida, restricciones y un caso que podría fallar.

## 2. Modificar

Prueba archivo ausente, JSON truncado y cantidad negativa. Registra la excepción de cada caso y el mensaje que mostrarías.

Registra qué cambiaste, por qué y qué resultado predijiste antes de ejecutar.

## 3. Transferir

Propón cómo guardar primero en un archivo temporal y reemplazar el destino solo al terminar. Explica por qué esto reduce escrituras incompletas y qué no resuelve.

Entrega una solución propia. Compara dos alternativas y explica por qué descartaste una.

## Evidencias

Entrega tu código cuando corresponda, una tabla con caso normal/límite/inválido, y una explicación individual de 100–150 palabras o audio de 1–2 minutos acordado con el docente. Para modelos sin código, usa una simulación de las reglas como evidencia.

| Entrada o situación | Resultado esperado y razón | Resultado obtenido | Ajuste |
|---|---|---|---|
| Normal: completar | | | |
| Límite: completar | | | |
| Inválido: completar | | | |

**Pista inicial:** Confiar en json.load como si validara las reglas del negocio permite cantidades negativas.

**Criterio específico:** Valida el esquema y no reemplaza silenciosamente datos dañados por un inventario vacío.

No basta con pegar una solución: debes explicar un paso y responder un cambio de requisito.
