# 02 · Colecciones, funciones y módulos

**Pregunta:** ¿Cómo resumir materiales de un proyecto sin duplicar código?

**Meta observable:** Separar responsabilidades con funciones y elegir entre lista, diccionario y conjunto.

**Sesiones 7–9:** tres encuentros de 120 minutos, adaptables. Prerrequisito: evidencias del módulo anterior.

## Conceptos con sentido

Una lista conserva elementos ordenados; un diccionario relaciona claves con valores; un conjunto representa elementos únicos. Una función recibe parámetros, realiza una responsabilidad y puede devolver un valor con return. print muestra información, pero no sustituye a return.

Una función que recibe los datos y devuelve un resultado es más fácil de probar que otra que pide entradas, calcula y muestra todo a la vez. Un módulo es un archivo Python importable. El bloque if __name__ == "__main__" permite ejecutar una demostración sin activarla al importar el archivo.

## Ruta de tres sesiones

| Sesión | Desarrollo | Evidencia |
|---|---|---|
| 7 · Comprender | 15 min problema; 25 actividad sin equipo; 25 explicación; 35 predicción y ejecución del ejemplo; 20 discusión | Descomposición y tabla de seguimiento |
| 8 · Modificar | 15 recuperación; 20 revisión del error frecuente; 60 taller niveles 1 y 2; 25 pruebas y explicación entre pares | Código modificado y casos de prueba |
| 9 · Transferir | 15 planeación; 60 reto nivel 3; 25 demostración individual; 20 retroalimentación | Solución propia, justificación y salida individual |

## Antes de ejecutar

Calcula el total de {"led": 4, "cable": 3}; luego el de {}. Señala qué recibe la función y qué devuelve.

Lee [el ejemplo](ejemplo.py), escribe tu predicción y después ejecuta desde la raíz:

```bash
python modulos/02_colecciones_funciones_y_modulos/ejemplo.py
```

Salida esperada:

```text
Unidades: 7
Inventario vacío: 0
```

En los primeros ejemplos aparecen funciones y validaciones que se profundizan después. Inicialmente sigue sus entradas y salidas; no se exige memorizar su sintaxis.

## Error para discutir

Retornar dentro de la primera iteración suma solo el primer material.

## Materiales y criterio de avance

- [Taller en tres niveles](taller.md).
- [Actividad sin computador](sin_computador.md).
- [Comprobación individual](evaluacion.md).
- [Orientaciones docentes](../../docente/solucionarios/02_colecciones_funciones_y_modulos.md): contienen respuestas; consultar después del intento.

**Avanza cuando:** Diferencia imprimir de retornar, contempla una colección vacía y comprueba que el filtro no modifica la entrada. Si no se cumple, repite un caso pequeño con tabla de seguimiento y presenta una explicación nueva.

[Anterior](../01_datos_decisiones_y_ciclos/README.md) · [Ruta general](../../README.md) · [Siguiente](../03_modelar_objetos/README.md)
