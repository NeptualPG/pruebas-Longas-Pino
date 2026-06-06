# Casos de Prueba Funcionales (Detallado)

Proyecto: JAANSTYLE
Módulos: Login, Maestro (CRUD), Transaccional

Formato por caso:
- ID: CA-XXX
- Título: breve descripción
- Prioridad: Alta/Media/Baja
- Precondiciones: datos / estado del sistema
- Pasos: lista numerada
- Resultado esperado: claro y verificable
- Evidencia: capturas / logs / respuestas API

---

## Login

- ID: CA-001
- Título: Login exitoso con 2FA
- Prioridad: Alta
- Precondiciones: Usuario `usuario.prueba@example.com` existe y `enabled=1`.
- Pasos:
  1. Enviar POST `/login` con email y contraseña válidos.
  2. Verificar respuesta indica generación de 2FA y devuelve token temporal.
  3. Consumir endpoint de verificación 2FA con token y código recibido (o tomar código desde logs en pruebas).
- Resultado esperado:
  - Paso 1: status 200 y mensaje que se envió código 2FA.
  - Paso 3: verificación 2FA exitosa y creación de sesión (session id / token válido).
- Evidencia: respuesta JSON, `ACCESS_LOG`, captura de pantalla del token/2FA en logs.

---

- ID: CA-002
- Título: Login con contraseña incorrecta
- Prioridad: Alta
- Precondiciones: Usuario existe.
- Pasos:
  1. Enviar POST `/login` con email correcto y contraseña incorrecta.
- Resultado esperado:
  - Status 401/400 según diseño; mensaje con "Credenciales inválidas"; no generar token 2FA.
- Evidencia: respuesta API y captura de logs.

---

- ID: CA-003
- Título: Bloqueo temporal tras intentos fallidos
- Prioridad: Alta
- Precondiciones: Usuario existe, contador de intentos en 0.
- Pasos:
  1. Intentar login con contraseña incorrecta 3 veces consecutivas.
  2. Intentar 4º login con contraseña correcta.
- Resultado esperado:
  - Tras 3 intentos: cuenta marcada como `blocked` y `blocked_until` establecido.
  - 4º intento: respuesta indicando "Cuenta bloqueada temporalmente".
- Evidencia: consulta a BD (`users.failed_attempts`, `users.blocked`), respuestas API.

---

- ID: CA-004
- Título: Login usuario inactivo
- Prioridad: Media
- Precondiciones: Usuario con `enabled = 0` existe.
- Pasos:
  1. Enviar POST `/login` con credenciales del usuario inactivo.
- Resultado esperado:
  - Respuesta que indica "Usuario deshabilitado" y no se genera 2FA.
- Evidencia: respuesta API y estado en BD.

---

## Maestro (CRUD)

- ID: CA-010
- Título: Listar registros del maestro
- Prioridad: Media
- Precondiciones: Existen registros en la tabla maestra; Authorization: Bearer `auth_token` válido.
- Pasos:
  1. Enviar GET `/maestro` con token válido.
- Resultado esperado:
  - Status 200 y lista (array) de items paginada o vacía.
- Evidencia: respuesta JSON, headers de paginación.

---

- ID: CA-011
- Título: Crear registro maestro válido
- Prioridad: Alta
- Precondiciones: Usuario con permisos de creación y datos válidos.
- Pasos:
  1. Enviar POST `/maestro` con payload válido.
- Resultado esperado:
  - Status 201/200 y respuesta contiene `id` del registro creado.
  - Registro visible en GET `/maestro/{id}`.
- Evidencia: respuesta JSON, consulta a BD.

---

- ID: CA-012
- Título: Crear registro maestro inválido (campos requeridos)
- Prioridad: Alta
- Precondiciones: Usuario con permisos de creación.
- Pasos:
  1. Enviar POST `/maestro` con campos vacíos o inválidos.
- Resultado esperado:
  - Status 400 y mensajes de validación indicando campos requeridos.
- Evidencia: respuesta JSON con errores.

---

- ID: CA-013
- Título: Editar registro maestro
- Prioridad: Media
- Precondiciones: Registro existente con `id_maestro`.
- Pasos:
  1. Enviar PUT `/maestro/{id_maestro}` con cambios válidos.
- Resultado esperado:
  - Status 200 y cambios reflejados en GET del recurso.
- Evidencia: respuesta JSON y consulta a BD.

---

- ID: CA-014
- Título: Eliminar registro maestro
- Prioridad: Media
- Precondiciones: Registro existente sin dependencias críticas.
- Pasos:
  1. Enviar DELETE `/maestro/{id_maestro}` con token válido.
- Resultado esperado:
  - Status 200/204 y el recurso ya no aparece en listados.
- Evidencia: respuesta y consulta a BD.

---

## Transaccional

- ID: CA-020
- Título: Registrar transacción válida
- Prioridad: Alta
- Precondiciones: FK a maestro existe, usuario autenticado con permisos, saldo/estado válido.
- Pasos:
  1. Enviar POST `/transaccion` con payload válido (fk_maestra, monto, datos usuario).
- Resultado esperado:
  - Status 200/201; respuesta con id de transacción y estado `completada` o `pendiente` según flujo.
  - Consumo idempotente si se reintenta con mismo request-id (si aplica).
- Evidencia: respuesta JSON y consulta a BD (`transaccional` table).

---

- ID: CA-021
- Título: Registrar transacción inválida (monto negativo)
- Prioridad: Alta
- Precondiciones: FK válido.
- Pasos:
  1. Enviar POST `/transaccion` con `monto <= 0`.
- Resultado esperado:
  - Status 400 y mensaje de validación.
- Evidencia: respuesta y registros de auditoría.

---

- ID: CA-022
- Título: Transacción y rollback en error de integridad
- Prioridad: Alta
- Precondiciones: Simular fallo en segundo paso del proceso transaccional.
- Pasos:
  1. Enviar flujo que genera error interno (forzar excepción en procesamiento).
  2. Verificar que la transacción se revierte y no quedan registros parciales.
- Resultado esperado:
  - Status 500 o error controlado; BD sin registros parciales (ver `pruebas-integridad.sql`).
- Evidencia: logs, capturas de DB comparativas antes/después.

---

## Consideraciones adicionales

- Preparar datos de prueba en `05-base-de-datos/datos-prueba.sql` antes de ejecutar funcionales.
- Registrar en `evidencias/` capturas, request/response, y el `test_report.json` ya generado.
- Para API: usar `04-pruebas-api/coleccion-postman.json` y crear `environment-postman.json` con `{{base_url}}`, `{{auth_token}}`, códigos esperados.

---

Archivo generado automáticamente por el asistente. Revisa y dime si quieres que ajuste prioridades, agregue más casos o genere la versión Markdown por módulo con plantillas imprimibles.
