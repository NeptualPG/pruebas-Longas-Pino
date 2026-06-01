# Guion para video screencast y video de presentacion

## A. Screencast tecnico (8 a 12 min)

## 1. Introduccion (0:00 - 1:00)

- Presentar proyecto [NombreProyecto].
- Explicar alcance: Login, Maestro CRUD, Transaccional.
- Mostrar estructura del repositorio de pruebas.

## 2. Plan y criterios (1:00 - 2:30)

- Mostrar archivo de plan de pruebas.
- Resaltar criterios Dado/Cuando/Entonces.
- Explicar trazabilidad entre criterios y casos.

## 3. Unitarias JUnit 5 (2:30 - 4:00)

- Abrir tests base de Login, Maestro y Transaccional.
- Mostrar placeholders a reemplazar.
- Ejecutar pruebas o simular ejecucion con resultado esperado.

## 4. Pruebas funcionales (4:00 - 5:30)

- Mostrar matriz de casos funcionales.
- Ejecutar al menos 1 caso de Login y 1 de Maestro o Transaccional.
- Registrar evidencia en carpeta correspondiente.

## 5. Pruebas API Postman (5:30 - 7:30)

- Abrir environment y coleccion.
- Mostrar variables clave (base_url, endpoints, token).
- Ejecutar requests y explicar pm.test.

## 6. Pruebas BD (7:30 - 9:30)

- Ejecutar datos-prueba.sql.
- Ejecutar pruebas-integridad.sql y revisar resultados esperados.
- Ejecutar pruebas-transacciones.sql (commit/rollback).

## 7. Cierre (9:30 - 10:30)

- Resumen de resultados.
- Defectos encontrados y estado.
- Siguientes pasos antes de entrega.

## B. Video de presentacion (4 a 6 min)

## 1. Problema y objetivo

- Que se evaluo y por que.
- Que modulos son criticos.

## 2. Enfoque de pruebas

- Estrategia aplicada por capas (unitaria, funcional, API, BD).
- Beneficios del enfoque.

## 3. Resultados clave

- Indicadores principales: ejecucion, aprobacion, defectos.
- Hallazgos importantes.

## 4. Valor para el proyecto

- Riesgos reducidos.
- Mejora en calidad y confiabilidad.

## 5. Cierre

- Recomendacion final.
- Trabajo pendiente.
