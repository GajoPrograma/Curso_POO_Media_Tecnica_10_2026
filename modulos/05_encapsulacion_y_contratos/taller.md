# Taller · Encapsulación, propiedades y contratos

Trabaja en pareja, pero cada integrante entrega su predicción y explicación. Cambien conductor y observador cada 15–20 minutos. En un trío, la tercera persona diseña pruebas y rota también.

## 1. Comprender

Escribe el contrato de retirar incluyendo tipo, rango, resultado y estado tras un error.

Antes de escribir código: identifica entradas, salida, restricciones y un caso que podría fallar.

## 2. Modificar

Implementa ingresar(cantidad), aceptando solo enteros positivos. Prueba 1, 0, -1 y True.

Registra qué cambiaste, por qué y qué resultado predijiste antes de ejecutar.

## 3. Transferir

Intenta asignar cantidad desde fuera y explica por qué la propiedad sin setter lo rechaza y por qué _cantidad sigue siendo accesible.

Entrega una solución propia. Compara dos alternativas y explica por qué descartaste una.

## Evidencias

Entrega tu código cuando corresponda, una tabla con caso normal/límite/inválido, y una explicación individual de 100–150 palabras o audio de 1–2 minutos acordado con el docente. Para modelos sin código, usa una simulación de las reglas como evidencia.

| Entrada o situación | Resultado esperado y razón | Resultado obtenido | Ajuste |
|---|---|---|---|
| Normal: completar | | | |
| Límite: completar | | | |
| Inválido: completar | | | |

**Pista inicial:** Restar antes de validar deja el objeto corrupto aunque luego se lance una excepción.

**Criterio específico:** Las operaciones rechazadas conservan el estado; diferencia convención de privacidad de control de acceso.

No basta con pegar una solución: debes explicar un paso y responder un cambio de requisito.
