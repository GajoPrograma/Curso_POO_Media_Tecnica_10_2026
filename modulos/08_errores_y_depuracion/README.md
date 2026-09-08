# 08 · Errores, excepciones y depuración

**Pregunta:** ¿Cómo responde un programa cuando se ingresa una cantidad imposible?

**Meta observable:** Distinguir errores de sintaxis, ejecución y lógica; localizar causas con evidencia.

**Sesiones 25–27:** tres encuentros de 120 minutos, adaptables. Prerrequisito: evidencias del módulo anterior.

## Conceptos con sentido

Un error de sintaxis impide interpretar el programa; uno de ejecución aparece durante una operación; uno de lógica produce un resultado incorrecto aunque no haya excepción. try/except permite tratar fallos previstos. raise comunica que no se cumple una regla.

La capa que conoce la regla genera el error; la interacción informa al usuario. Capturar Exception sin una razón concreta puede ocultar fallos de programación. Depurar exige reproducir, formular una hipótesis, inspeccionar valores, cambiar una causa y volver a probar. El traceback muestra la ruta de llamadas y el lugar del fallo.

## Ruta de tres sesiones

| Sesión | Desarrollo | Evidencia |
|---|---|---|
| 25 · Comprender | 15 min problema; 25 actividad sin equipo; 25 explicación; 35 predicción y ejecución del ejemplo; 20 discusión | Descomposición y tabla de seguimiento |
| 26 · Modificar | 15 recuperación; 20 revisión del error frecuente; 60 taller niveles 1 y 2; 25 pruebas y explicación entre pares | Código modificado y casos de prueba |
| 27 · Transferir | 15 planeación; 60 reto nivel 3; 25 demostración individual; 20 retroalimentación | Solución propia, justificación y salida individual |

## Antes de ejecutar

Clasifica "3", "0", "hola" y "2.5": ¿falla la conversión o la regla de positividad?

Lee [el ejemplo](ejemplo.py), escribe tu predicción y después ejecuta desde la raíz:

```bash
python modulos/08_errores_y_depuracion/ejemplo.py
```

Salida esperada:

```text
3
La cantidad debe ser positiva
Escribe un número entero
Escribe un número entero
```

En los primeros ejemplos aparecen funciones y validaciones que se profundizan después. Inicialmente sigue sus entradas y salidas; no se exige memorizar su sintaxis.

## Error para discutir

Usar except: pass hace desaparecer el síntoma y puede simular que una operación sí ocurrió.

## Materiales y criterio de avance

- [Taller en tres niveles](taller.md).
- [Actividad sin computador](sin_computador.md).
- [Comprobación individual](evaluacion.md).
- [Orientaciones docentes](../../docente/solucionarios/08_errores_y_depuracion.md): contienen respuestas; consultar después del intento.

**Avanza cuando:** Captura excepciones específicas y aporta un caso reproducible que demuestra la corrección. Si no se cumple, repite un caso pequeño con tabla de seguimiento y presenta una explicación nueva.

[Anterior](../07_herencia_polimorfismo_y_abstraccion/README.md) · [Ruta general](../../README.md) · [Siguiente](../09_archivos_y_persistencia/README.md)
