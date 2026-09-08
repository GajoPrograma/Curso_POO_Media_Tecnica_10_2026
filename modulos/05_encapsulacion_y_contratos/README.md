# 05 · Encapsulación, propiedades y contratos

**Pregunta:** ¿Cómo evitar que un inventario termine con existencias negativas?

**Meta observable:** Mantener invariantes a través de métodos y explicar límites de la privacidad en Python.

**Sesiones 16–18:** tres encuentros de 120 minutos, adaptables. Prerrequisito: evidencias del módulo anterior.

## Conceptos con sentido

Encapsular significa ofrecer operaciones que mantienen las reglas del objeto. Una invariante debe seguir siendo verdadera después de cada operación pública. Un contrato describe precondiciones, resultado y errores. _cantidad señala uso interno por convención; no es una barrera de seguridad.

Una propiedad permite consultar un dato sin ofrecer un setter. La cantidad se cambia mediante retirar, que comprueba primero la solicitud y solo después modifica el estado. Un setter para cada atributo no garantiza encapsulación: lo importante es que ninguna operación pública deje un estado inválido.

## Ruta de tres sesiones

| Sesión | Desarrollo | Evidencia |
|---|---|---|
| 16 · Comprender | 15 min problema; 25 actividad sin equipo; 25 explicación; 35 predicción y ejecución del ejemplo; 20 discusión | Descomposición y tabla de seguimiento |
| 17 · Modificar | 15 recuperación; 20 revisión del error frecuente; 60 taller niveles 1 y 2; 25 pruebas y explicación entre pares | Código modificado y casos de prueba |
| 18 · Transferir | 15 planeación; 60 reto nivel 3; 25 demostración individual; 20 retroalimentación | Solución propia, justificación y salida individual |

## Antes de ejecutar

Con cantidad 5: retirar 2, intentar retirar 4, consultar cantidad. Predice el estado tras el error.

Lee [el ejemplo](ejemplo.py), escribe tu predicción y después ejecuta desde la raíz:

```bash
python modulos/05_encapsulacion_y_contratos/ejemplo.py
```

Salida esperada:

```text
Existencias insuficientes
Unidades: 3
```

En los primeros ejemplos aparecen funciones y validaciones que se profundizan después. Inicialmente sigue sus entradas y salidas; no se exige memorizar su sintaxis.

## Error para discutir

Restar antes de validar deja el objeto corrupto aunque luego se lance una excepción.

## Materiales y criterio de avance

- [Taller en tres niveles](taller.md).
- [Actividad sin computador](sin_computador.md).
- [Comprobación individual](evaluacion.md).
- [Orientaciones docentes](../../docente/solucionarios/05_encapsulacion_y_contratos.md): contienen respuestas; consultar después del intento.

**Avanza cuando:** Las operaciones rechazadas conservan el estado; diferencia convención de privacidad de control de acceso. Si no se cumple, repite un caso pequeño con tabla de seguimiento y presenta una explicación nueva.

[Anterior](../04_clases_e_instancias/README.md) · [Ruta general](../../README.md) · [Siguiente](../06_composicion_y_colaboracion/README.md)
