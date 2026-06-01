# Casos de prueba

Completar las columnas Resultado real y Estado durante la ejecucion.
Estado permitido: Paso, Fallo o Bloqueado.

## Modulo: Login

| ID | Descripcion | Precondicion | Pasos | Resultado esperado | Resultado real | Estado |
|---|---|---|---|---|---|---|
| CP-001 | Login exitoso | Usuario activo registrado | 1. Ingresar usuario valido 2. Ingresar contrasena correcta 3. Clic en Ingresar | Redirige al menu principal | [resultado_real] | [estado] |
| CP-002 | Login con contrasena incorrecta | Usuario activo registrado | 1. Ingresar usuario valido 2. Ingresar contrasena incorrecta 3. Clic en Ingresar | Muestra mensaje de error sin revelar cual campo es incorrecto | [resultado_real] | [estado] |
| CP-003 | Login con usuario inexistente | Ninguna | 1. Ingresar usuario que no existe 2. Ingresar cualquier contrasena 3. Clic en Ingresar | Muestra mensaje de error generico | [resultado_real] | [estado] |
| CP-004 | Login con campos vacios | Ninguna | 1. Dejar ambos campos vacios 2. Clic en Ingresar | El sistema muestra validacion sin enviar la peticion | [resultado_real] | [estado] |
| CP-005 | Login con usuario inactivo | Usuario inactivo en BD | 1. Ingresar credenciales de usuario inactivo 2. Clic en Ingresar | El sistema rechaza el acceso con mensaje apropiado | [resultado_real] | [estado] |

## Modulo: Maestro (CRUD)

| ID | Descripcion | Precondicion | Pasos | Resultado esperado | Resultado real | Estado |
|---|---|---|---|---|---|---|
| CP-006 | Crear registro valido | Sesion activa | 1. Ir al modulo maestro 2. Clic en Nuevo 3. Llenar campos 4. Guardar | Registro aparece en listado con datos ingresados | [resultado_real] | [estado] |
| CP-007 | Crear registro con campo obligatorio vacio | Sesion activa | 1. Ir al modulo maestro 2. Clic en Nuevo 3. Dejar campo obligatorio vacio 4. Guardar | El sistema muestra validacion y no guarda | [resultado_real] | [estado] |
| CP-008 | Editar registro existente | Registro [codigo_test] en BD | 1. Buscar registro 2. Clic en Editar 3. Modificar campo 4. Guardar | Cambios se reflejan en listado y BD | [resultado_real] | [estado] |
| CP-009 | Eliminar registro sin dependencias | Registro sin transacciones asociadas | 1. Buscar registro 2. Clic en Eliminar 3. Confirmar | Registro desaparece de listado y BD | [resultado_real] | [estado] |
| CP-010 | Eliminar registro con dependencias | Registro con transacciones asociadas | 1. Buscar registro con uso 2. Clic en Eliminar 3. Confirmar | El sistema impide eliminacion y muestra mensaje | [resultado_real] | [estado] |

## Modulo: Transaccional

| ID | Descripcion | Precondicion | Pasos | Resultado esperado | Resultado real | Estado |
|---|---|---|---|---|---|---|
| CP-011 | Registrar transaccion valida | Sesion activa, datos de prueba en BD | 1. Ir a modulo transaccional 2. Llenar campos validos 3. Confirmar | Transaccion se registra y estado en BD es [estado_completada] | [resultado_real] | [estado] |
| CP-012 | Registrar transaccion con monto invalido | Sesion activa | 1. Ir a modulo transaccional 2. Ingresar monto negativo o cero 3. Confirmar | El sistema rechaza la operacion con validacion | [resultado_real] | [estado] |
| CP-013 | Acceso sin sesion activa | Ninguna sesion activa | 1. Copiar URL de modulo 2. Cerrar sesion 3. Pegar URL | El sistema redirige al login sin mostrar modulo | [resultado_real] | [estado] |
| CP-014 | Registrar transaccion con campos vacios | Sesion activa | 1. Ir a modulo transaccional 2. Dejar campos obligatorios vacios 3. Confirmar | El sistema muestra validacion y no procesa transaccion | [resultado_real] | [estado] |
| CP-015 | Verificar registro en BD tras transaccion | Transaccion CP-011 ejecutada | 1. Abrir cliente BD 2. Consultar [tabla_transaccional] 3. Buscar registro | El registro existe con datos correctos y estado [estado_completada] | [resultado_real] | [estado] |