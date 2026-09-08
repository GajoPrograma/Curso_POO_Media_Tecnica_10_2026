# Proyecto 03 · Inventario de materiales de robótica

**Necesidad:** registrar materiales, entradas y retiros sin existencias negativas y recuperar el estado al reiniciar. Se utilizan datos ficticios de materiales, no datos de estudiantes. Aplicación educativa local para un solo proceso.

## Ejecutar

Desde la raíz:

```bash
python proyectos/03_inventario_poo/main.py
```

Secuencia de prueba: opción 2 → código M1 → nombre Relé → cantidad 5; opción 4 → M1 → 2; opción 1 muestra cantidad 3; opción 5 guarda; opción 0 sale. Ejecuta de nuevo y consulta: conserva 3. Intentar retirar 4 debe rechazarse y mantener 3.

El archivo queda en `proyectos/03_inventario_poo/datos_locales/inventario.json`, ignorado por Git. Solo Guardar persiste cambios. Si sales con cambios pendientes, el menú pide decidir si los descartas. Si el archivo está dañado, el arranque se detiene para que puedas revisarlo; no lo reemplaza por datos vacíos.

## Responsabilidades

| Archivo | Responsabilidad | No debe hacer |
|---|---|---|
| dominio.py | Material mantiene cantidades válidas; Inventario coordina por código | Leer teclado o abrir archivos |
| persistencia.py | Guardar y reconstruir datos validados | Decidir reglas de existencias |
| main.py | Interpretar opciones y comunicar resultados | Modificar atributos internos |

Material usa propiedades; Inventario crea y coordina sus materiales. La persistencia reconstruye mediante los mismos contratos. No añadimos herencia porque esta versión no tiene subtipos que la necesiten.

## Requisitos y aceptación

| ID | Regla | Ejemplo verificable |
|---|---|---|
| INV-01 | Código y nombre no vacíos; código único | Repetir M1 genera rechazo |
| INV-02 | Cantidad inicial entera no negativa | 0 válido; -1, True y 2.5 inválidos |
| INV-03 | Entrada y retiro enteros positivos | 1 válido; 0 y -1 inválidos |
| INV-04 | Retiro no supera existencias | Retirar 5 de 5 deja 0; retirar 6 de 5 conserva 5 |
| INV-05 | Código inexistente genera error | Retirar de AUSENTE no cambia otro material |
| INV-06 | Guardar y cargar conserva datos | Nombre con tilde y cantidad se recuperan |
| INV-07 | Archivo inválido no se acepta parcialmente | Duplicado o cantidad negativa rechaza toda la carga |
| INV-08 | Las consultas no permiten alterar el inventario | Modificar listar() no cambia el objeto |

## Iteraciones dentro del curso

1. Desde módulo 05: redacta contratos y dibuja Material; no copies aún el código.
2. Módulo 06: agrega Inventario y delegación; prueba en memoria.
3. Módulos 08–09: comunica errores y guarda JSON; compara archivo ausente y dañado.
4. Módulos 10–11: ejecuta pruebas, agrega las extensiones y sustenta.

## Trabajo que debe crear el estudiante

- Búsqueda pública por código que devuelva datos de consulta, con contrato para ausentes.
- Reporte de existencias bajas: definir si incluye el umbral y probarlo.
- Al menos seis requisitos vinculados a pruebas; incluir las dos extensiones.
- Un cambio propio acordado con el docente: por ejemplo, categoría o reserva. Analizar impacto antes de implementarlo.

## Defensa individual

Explica por qué no cambia el estado tras un retiro rechazado; señala dónde se valida JSON; predice qué pasa con un booleano como cantidad; modifica un criterio del reporte sin romper sus pruebas. Usa la rúbrica común.

## Límites de la referencia

No incluye autenticación, movimientos históricos, concurrencia ni copias de seguridad. El reemplazo de archivo temporal evita dejar un JSON parcial durante la escritura normal, pero no garantiza recuperación ante todos los fallos del sistema ni coordina dos programas escribiendo a la vez. No se guardan automáticamente los cambios al interrumpir con Ctrl+C.
