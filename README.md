# pruebas-[apellido1]-[apellido2]

Guia operativa para planificar, ejecutar y documentar pruebas de software sobre un proyecto web real con tres modulos:

1. Login
2. Modulo maestro CRUD
3. Modulo transaccional

Este repositorio ya esta separado por fases. La documentacion base esta creada, pero varios artefactos todavia tienen placeholders o estan pendientes de cierre final.

## Tabla de contenido

1. Descripcion general de la actividad
2. Herramientas requeridas
3. Estructura del repositorio
4. Fase 1 - Planificacion y criterios de aceptacion
5. Fase 2 - Pruebas unitarias con JUnit 5
6. Fase 3 - Pruebas funcionales con Selenium IDE
7. Fase 4 - Pruebas de API con Postman
8. Fase 5 - Pruebas de base de datos con MySQL Workbench
9. Fase 6 - Pruebas de seguridad con OWASP ZAP
10. Scripts SQL paso a paso
11. Casos de prueba
12. Plantilla de reporte de bugs
13. Requisitos de evidencia anti-IA
14. Checklist de entrega
15. Criterios de calificacion

## 1. Descripcion general de la actividad

Esta actividad evalua la capacidad de dos estudiantes para planificar, ejecutar y documentar pruebas de software en 25 horas distribuidas en 6 fases.

Objetivo general:

- Aplicar tecnicas de pruebas manuales y automatizadas sobre el sistema real del equipo.

Objetivos especificos:

- Elaborar plan de pruebas y criterios de aceptacion.
- Ejecutar pruebas unitarias, funcionales, API, BD y seguridad.
- Registrar evidencias verificables con marca de tiempo.
- Reportar defectos con formato estandar.
- Organizar artefactos en Git con estructura definida.

Distribucion de tiempo:

| Fase | Actividad | Horas |
|---|---|---|
| 1 | Planificacion y criterios de aceptacion | 3 |
| 2 | Pruebas unitarias con JUnit 5 | 5 |
| 3 | Pruebas funcionales con Selenium IDE | 5 |
| 4 | Pruebas de API con Postman | 4 |
| 5 | Pruebas de BD con MySQL Workbench | 4 |
| 6 | Pruebas de seguridad con OWASP ZAP | 2 |
| - | Consolidacion, reporte final y video | 2 |
| - | TOTAL | 25 |

## 2. Herramientas requeridas

| Herramienta | Uso |
|---|---|
| JUnit 5 | Pruebas unitarias backend |
| Selenium IDE | Pruebas funcionales navegador |
| Postman | Pruebas API REST |
| MySQL Workbench | Pruebas de base de datos |
| OWASP ZAP | Pruebas de seguridad |
| OBS Studio | Grabacion de evidencias |
| Git + GitHub/GitLab | Control de versiones y entrega |

## 3. Estructura del repositorio

Se debe conservar esta estructura minima:

- `01-planificacion/`
- `02-pruebas-unitarias/`
- `03-pruebas-funcionales/`
- `04-pruebas-api/`
- `05-base-de-datos/`
- `06-seguridad/`
- `07-entrega-final/`

Estado actual resumido:

- `01-planificacion/`: documentos base creados.
- `02-pruebas-unitarias/`: clases de prueba creadas, pero aun con placeholders.
- `03-pruebas-funcionales/`: suite y casos base creados; evidencias incompletas.
- `04-pruebas-api/`: coleccion, environment, reporte y capturas base creadas.
- `05-base-de-datos/`: scripts y capturas base creadas; falta adaptar nombres reales.
- `06-seguridad/`: guia, reporte y capturas base creadas.
- `07-entrega-final/`: reporte final y screencast parcial; falta el video de presentacion y los reportes de bugs completos.

Convencion de commits por fase:

- [FASE-1] Plan de pruebas y criterios de aceptacion
- [FASE-2] Pruebas unitarias JUnit - modulo Login
- [FASE-2] Pruebas unitarias JUnit - modulo Maestro
- [FASE-2] Pruebas unitarias JUnit - modulo Transaccional
- [FASE-3] Casos de prueba funcionales ejecutados y evidencias
- [FASE-4] Coleccion Postman y reporte de API
- [FASE-5] Scripts SQL y evidencias de base de datos
- [FASE-6] Reporte OWASP ZAP
- [FASE-7] Reporte final y videos

## 4. Fase 1 - Planificacion y criterios de aceptacion

Entregables:

- `01-planificacion/plan-de-pruebas.md`
- `01-planificacion/criterios-aceptacion.md`

Regla minima:

- Al menos 20 criterios en formato Dado/Cuando/Entonces.

## 5. Fase 2 - Pruebas unitarias con JUnit 5

Alcance:

- Probar logica de negocio de Login, Maestro y Transaccional.

Minimos:

- Al menos 5 metodos por clase.
- Al menos 20 pruebas unitarias totales.

Nota actual:

- Las clases Java existen, pero todavia usan ejemplos y placeholders en vez de la logica real del sistema.

## 6. Fase 3 - Pruebas funcionales con Selenium IDE

Entregables:

- `03-pruebas-funcionales/selenium-suite.side`
- `03-pruebas-funcionales/casos-prueba-funcionales.md`
- Evidencias por caso en `03-pruebas-funcionales/evidencias/`.

Nota actual:

- La separacion por carpeta ya existe, pero faltan capturas por cada caso ejecutado.

## 7. Fase 4 - Pruebas de API con Postman

Minimo esperado:

- Requests de Login, Maestro y Transaccional con pruebas en `pm.test`.
- Export de coleccion y environment:
	- `04-pruebas-api/coleccion-postman.json`
	- `04-pruebas-api/environment-postman.json`

Nota actual:

- La coleccion existe, pero sigue usando variables y endpoints genericos.

## 8. Fase 5 - Pruebas de base de datos con MySQL Workbench

Orden de ejecucion:

1. `05-base-de-datos/datos-prueba.sql`
2. `05-base-de-datos/pruebas-integridad.sql`
3. `05-base-de-datos/pruebas-transacciones.sql`

Nota actual:

- Los scripts estan separados, pero aun usan placeholders y necesitan adaptacion al esquema real.

## 9. Fase 6 - Pruebas de seguridad con OWASP ZAP

Entregables:

- `06-seguridad/reporte-zap.html`
- Evidencias en `06-seguridad/evidencias/`.

## 10. Scripts SQL paso a paso

Todos los scripts usan placeholders y deben adaptarse a nombres reales:

- [tabla_usuarios]
- [tabla_maestra]
- [tabla_transaccional]
- [campo_x]

## 11. Casos de prueba

Los casos funcionales se ejecutan y se completan con:

- Resultado real
- Estado (Paso, Fallo, Bloqueado)

Archivo base:

- `03-pruebas-funcionales/casos-prueba-funcionales.md`

## 12. Plantilla de reporte de bugs

Archivo base:

- `07-entrega-final/plantillas-reporte-bugs.md`

Se esperan al menos 3 reportes de bug reales.

## 13. Requisitos de evidencia anti-IA

Reglas obligatorias:

- Capturas con hora visible del sistema.
- SQL y pruebas apuntando al proyecto real.
- Requests Postman con URLs reales del sistema.
- Video screencast mostrando ejecucion real.

## 14. Checklist de entrega

Usar checklist de validacion final antes de enviar:

- Estructura completa.
- Evidencias completas.
- Minimos de pruebas cumplidos.
- Commits por fase realizados.

## 15. Criterios de calificacion

Rubrica sugerida (ajustar a lineamientos del docente):

- Fase 1: 15%
- Fase 2: 20%
- Fase 3: 20%
- Fase 4: 15%
- Fase 5: 15%
- Fase 6: 10%
- Entrega final y calidad de evidencia: 5%

## Regla clave de adaptacion

No dejar placeholders en entrega final. Todo valor entre corchetes debe ser reemplazado con informacion real del proyecto.
