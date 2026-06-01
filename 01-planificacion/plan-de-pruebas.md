# Plan de Pruebas - [NombreProyecto]

## 1. Informacion general

- Sistema: [NombreSistema]
- Version bajo prueba: [version]
- Ambiente objetivo: [qa|staging|local]
- Responsable QA: [nombre_qa]
- Fecha: [aaaa-mm-dd]

Descripcion breve:

[Descripcion del sistema web y su objetivo funcional]

## 2. Modulos en alcance

1. Login
2. Modulo maestro CRUD
3. Modulo transaccional

Fuera de alcance:

- [modulo_fuera_alcance_1]
- [modulo_fuera_alcance_2]

## 3. Objetivos de prueba

- Validar autenticacion y control de acceso en Login.
- Validar operaciones CRUD sobre entidades maestras.
- Validar reglas de negocio del modulo transaccional.
- Verificar integridad de datos y consistencia transaccional.
- Detectar defectos funcionales, de datos y de API antes de entrega.

## 4. Tipos de prueba

- Unitarias (JUnit 5)
- Funcionales (manuales o automatizadas)
- API (Postman + pm.test)
- Base de datos (scripts SQL)
- Seguridad basica (opcional en esta actividad)

## 5. Matriz modulo vs tipo de prueba

| Modulo | Unitarias | Funcionales | API | BD |
|---|---|---|---|---|
| Login | Si | Si | Si | Si |
| Maestro CRUD | Si | Si | Si | Si |
| Transaccional | Si | Si | Si | Si |

## 6. Criterios de entrada

- Codigo desplegado en [ambiente_prueba].
- Base de datos de prueba disponible y respaldada.
- Usuarios y roles de prueba creados.
- Endpoints publicados o documentados.
- Datos iniciales cargados.

## 7. Criterios de salida

- Casos planificados ejecutados al 100%.
- Defectos criticos y altos corregidos o justificados.
- Evidencias anexas por modulo (capturas, logs, reportes).
- Reporte final consolidado y firmado por [responsable].

## 8. Riesgos y mitigacion

| Riesgo | Impacto | Probabilidad | Mitigacion |
|---|---|---|---|
| Datos de prueba incompletos | Alto | Media | Script de carga controlada y validacion previa |
| Ambiente inestable | Alto | Media | Ventana de ejecucion y checkpoint por lote |
| Cambios tardios de requisitos | Medio | Alta | Congelar alcance por iteracion |
| Dependencias externas no disponibles | Medio | Media | Mock o sandbox de [servicio_externo] |

## 9. Cronograma sugerido

| Fase | Actividad | Duracion estimada |
|---|---|---|
| 1 | Planificacion y criterios | [x] dias |
| 2 | Unitarias JUnit 5 | [x] dias |
| 3 | Funcionales | [x] dias |
| 4 | API Postman | [x] dias |
| 5 | BD integridad y transacciones | [x] dias |
| 6 | Consolidacion y entrega final | [x] dias |

## 10. Herramientas

- IDE: [IDE]
- Build Java: [Maven|Gradle]
- Unit testing: JUnit 5
- API testing: Postman
- DB client: [cliente_bd]
- Gestion evidencias: [ruta_evidencias]

## 11. Entregables

- Plan de pruebas.
- Criterios de aceptacion.
- Casos funcionales.
- Pruebas unitarias base JUnit 5.
- Scripts SQL de prueba.
- Coleccion Postman con pm.test.
- Reporte final.
- Guion de videos.
