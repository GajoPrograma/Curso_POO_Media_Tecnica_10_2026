# Taller · Pruebas y diseño mantenible

Trabaja en pareja, pero cada integrante entrega su predicción y explicación. Cambien conductor y observador cada 15–20 minutos. En un trío, la tercera persona diseña pruebas y rota también.

## 1. Comprender

Agrega una prueba de retiro exacto que deje saldo cero.

Antes de escribir código: identifica entradas, salida, restricciones y un caso que podría fallar.

## 2. Modificar

Agrega una prueba que confirme que un retiro rechazado no cambia el saldo, y una de independencia entre cuentas.

Registra qué cambiaste, por qué y qué resultado predijiste antes de ejecutar.

## 3. Transferir

Refactoriza un programa que mezcla input y cálculo en dominio.py y main.py. Ejecuta las mismas pruebas antes y después y explica la dependencia eliminada.

Entrega una solución propia. Compara dos alternativas y explica por qué descartaste una.

## Evidencias

Entrega tu código cuando corresponda, una tabla con caso normal/límite/inválido, y una explicación individual de 100–150 palabras o audio de 1–2 minutos acordado con el docente. Para modelos sin código, usa una simulación de las reglas como evidencia.

| Entrada o situación | Resultado esperado y razón | Resultado obtenido | Ajuste |
|---|---|---|---|
| Normal: completar | | | |
| Límite: completar | | | |
| Inválido: completar | | | |

**Pista inicial:** Probar solo que se creó un objeto no demuestra que proteja sus invariantes.

**Criterio específico:** Cada prueba corresponde a una regla identificable; una refactorización conserva resultados y errores esperados.

No basta con pegar una solución: debes explicar un paso y responder un cambio de requisito.
