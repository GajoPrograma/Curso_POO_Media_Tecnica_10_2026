# Evolución del curso

El docente mantiene la secuencia y los criterios pedagógicos. Para proponer un cambio:

1. Describe la dificultad observada sin datos personales y el resultado esperado.
2. Crea una rama como mejora/m05-retiros; modifica solo los materiales relacionados.
3. Conserva explicaciones, ejemplo ejecutable, taller, evaluación y orientación docente coherentes.
4. Ejecuta `python herramientas/verificar_curso.py` y `python -m unittest discover -s tests -v`.
5. Actualiza CHANGELOG.md y ESTADO_CURSO.md cuando corresponda.
6. Abre una solicitud de cambios con motivo, contenido y evidencia; revisa antes de integrar a main.

No elimines respuestas de estudiantes ni reescribas historia compartida. La rama principal debe contener material utilizable. Los cambios grandes de secuencia requieren explicar qué prerrequisitos y sesiones se modifican. Numeración propuesta: corrección 1.0.1, ampliación compatible 1.1.0, reorganización incompatible 2.0.0.

Para retomar con un asistente: “Lee README.md, ESTADO_CURSO.md, PLAN_CURRICULAR.md y CHANGELOG.md en este repositorio. Revisa el módulo indicado, mejora sus materiales a partir de esta evidencia de clase: [...]. Conserva el trabajo existente, verifica ejemplos y pruebas y registra los cambios”.
