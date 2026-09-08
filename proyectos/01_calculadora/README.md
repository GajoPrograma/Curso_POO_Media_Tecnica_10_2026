# Proyecto 01 · Calculadora robusta

**Problema:** realizar operaciones e informar entradas inválidas sin cerrar inesperadamente. No necesita clases: primero aprende a separar responsabilidades. Integrar en sesiones 8–9 y revisar errores en 25–27.

## Ejecutar desde la raíz

```bash
python proyectos/01_calculadora/main.py
```

Prueba operador `+`, números `2` y `3`: resultado `5.0`. Prueba `/`, `5` y `0`: mensaje de error y vuelve al menú. Usa `salir` como operador.

## Requisitos de referencia

| ID | Regla | Evidencia |
|---|---|---|
| CAL-01 | Sumar, restar, multiplicar y dividir | 2+3=5; 5-2=3; 3*4=12; 5/2=2.5 |
| CAL-02 | Rechazar división por cero | 5/0 produce error; 0/5 produce 0 |
| CAL-03 | Rechazar operador desconocido y números no finitos | ^, nan e inf no se aceptan |
| CAL-04 | Interfaz independiente de operaciones | Importar operaciones no solicita entrada |

## Entregas por etapas

1. Papel: contratos y tabla de al menos seis casos antes de ver el código.
2. Funciones: construye tu solución y compárala con operaciones.py.
3. Interacción: incorpora el menú; demuestra recuperación después de una entrada inválida.

## Taller de ampliación

Agrega historial de operaciones exitosas y consulta del historial sin recalcular. Decide si una operación fallida aparece en el historial y justifica. Luego agrega potencia con límites explícitos para no aceptar resultados complejos o desbordamientos silenciosos.

Entrega instrucciones, pruebas y explicación individual: ¿por qué no hace falta una clase Calculadora en esta primera versión? Los float pueden tener aproximaciones; este proyecto no es una calculadora financiera.
