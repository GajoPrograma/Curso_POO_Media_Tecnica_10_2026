# 07 · Herencia, polimorfismo y abstracción

**Pregunta:** ¿Cómo enviar un aviso por distintos medios sin cambiar quien lo solicita?

**Meta observable:** Usar un contrato común y justificar cuándo una jerarquía facilita o perjudica el diseño.

**Sesiones 22–24:** tres encuentros de 120 minutos, adaptables. Prerrequisito: evidencias del módulo anterior.

## Conceptos con sentido

Herencia expresa una relación de subtipo: una implementación debe poder usarse donde se espera el tipo base sin romper su contrato. Polimorfismo permite la misma operación sobre objetos con implementaciones distintas. La abstracción conserva lo relevante para el cliente y oculta detalles que no necesita.

Una clase abstracta define una operación obligatoria mediante ABC y abstractmethod. Python también permite polimorfismo por comportamiento, sin base común. super() delega al siguiente método según el orden de resolución; en una jerarquía sencilla suele usarse para inicializar la base. Heredar solo para reutilizar unas líneas no es una justificación suficiente.

## Ruta de tres sesiones

| Sesión | Desarrollo | Evidencia |
|---|---|---|
| 22 · Comprender | 15 min problema; 25 actividad sin equipo; 25 explicación; 35 predicción y ejecución del ejemplo; 20 discusión | Descomposición y tabla de seguimiento |
| 23 · Modificar | 15 recuperación; 20 revisión del error frecuente; 60 taller niveles 1 y 2; 25 pruebas y explicación entre pares | Código modificado y casos de prueba |
| 24 · Transferir | 15 planeación; 60 reto nivel 3; 25 demostración individual; 20 retroalimentación | Solución propia, justificación y salida individual |

## Antes de ejecutar

Predice los mensajes al recorrer ambos notificadores. Explica por qué avisar no pregunta por el tipo.

Lee [el ejemplo](ejemplo.py), escribe tu predicción y después ejecuta desde la raíz:

```bash
python modulos/07_herencia_polimorfismo_y_abstraccion/ejemplo.py
```

Salida esperada:

```text
Pantalla: Devolver L1
Simulado: Devolver L1
```

En los primeros ejemplos aparecen funciones y validaciones que se profundizan después. Inicialmente sigue sus entradas y salidas; no se exige memorizar su sintaxis.

## Error para discutir

Una jerarquía larga no implica un mejor modelo; si el subtipo rechaza todos los casos válidos no es sustituible.

## Materiales y criterio de avance

- [Taller en tres niveles](taller.md).
- [Actividad sin computador](sin_computador.md).
- [Comprobación individual](evaluacion.md).
- [Orientaciones docentes](../../docente/solucionarios/07_herencia_polimorfismo_y_abstraccion.md): contienen respuestas; consultar después del intento.

**Avanza cuando:** Añade una implementación sin condicionales por tipo y justifica sustitución con ejemplos. Si no se cumple, repite un caso pequeño con tabla de seguimiento y presenta una explicación nueva.

[Anterior](../06_composicion_y_colaboracion/README.md) · [Ruta general](../../README.md) · [Siguiente](../08_errores_y_depuracion/README.md)
