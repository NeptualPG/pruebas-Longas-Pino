# Plantillas de reporte de bugs

## Plantilla 1: Bug funcional

- ID: BUG-[MOD]-[NNN]
- Titulo: [Resumen corto y accionable]
- Modulo: [Login|Maestro|Transaccional]
- Severidad: [Critica|Alta|Media|Baja]
- Prioridad: [Alta|Media|Baja]
- Ambiente: [qa|staging|local] - [navegador/version o app/version]
- Build/Version: [version_sistema]
- Precondiciones:
  - [precondicion_1]
  - [precondicion_2]
- Pasos para reproducir:
  1. [paso_1]
  2. [paso_2]
  3. [paso_3]
- Resultado actual: [que ocurre realmente]
- Resultado esperado: [que deberia ocurrir]
- Evidencia: [ruta_captura_log_video]
- Datos de prueba usados: [usuarios/ids/payload]
- Impacto de negocio: [impacto]
- Estado: [Nuevo|En analisis|En progreso|Resuelto|Cerrado]
- Asignado a: [responsable]
- Fecha reporte: [aaaa-mm-dd]

## Plantilla 2: Bug API

- ID: BUG-API-[NNN]
- Endpoint: [metodo] [endpoint]
- Tipo bug: [Contrato|Validacion|Auth|Performance|Manejo de errores]
- Request headers: [headers]
- Request body: [payload]
- Response actual: [status/body]
- Response esperada: [status/body]
- Caso de prueba asociado: [CP-XXX-YY]
- Evidencia Postman: [coleccion/reporte]
- Observaciones tecnicas: [detalle]

## Plantilla 3: Bug BD

- ID: BUG-BD-[NNN]
- Tabla(s): [tabla_1], [tabla_2]
- Tipo bug: [Integridad|Transaccion|Duplicidad|Nulos|Performance]
- Script ejecutado: [archivo_sql]
- Query de reproduccion: [sql]
- Resultado actual: [resultado]
- Resultado esperado: [resultado]
- Evidencia: [captura_resultset]
- Riesgo: [alto/medio/bajo]
