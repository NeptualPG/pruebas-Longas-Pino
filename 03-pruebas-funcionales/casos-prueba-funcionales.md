# Casos de Prueba Funcionales - Jeanstyle

## Módulo: Login

| ID     | Descripción                     | Precondición                    | Pasos                                                                         | Resultado esperado                 | Resultado real                 | Estado   |
| ------ | ------------------------------- | ------------------------------- | ----------------------------------------------------------------------------- | ---------------------------------- | ------------------------------ | -------- |
| CP-001 | Login exitoso                   | Usuario registrado y habilitado | 1. Ingresar correo válido 2. Ingresar contraseña correcta 3. Clic en Ingresar | Acceso exitoso al Dashboard        | Acceso correcto al sistema     | Paso     |
| CP-002 | Login con contraseña incorrecta | Usuario registrado              | 1. Ingresar correo válido 2. Contraseña incorrecta 3. Clic en Ingresar        | Mensaje de error y acceso denegado | Mensaje mostrado correctamente | Paso     |
| CP-003 | Login con usuario inexistente   | Ninguna                         | 1. Ingresar correo inexistente 2. Contraseña cualquiera 3. Ingresar           | Mensaje de credenciales inválidas  | [resultado_real]               | [estado] |
| CP-004 | Login con campos vacíos         | Ninguna                         | 1. Dejar campos vacíos 2. Ingresar                                            | Validación HTML obligatoria        | [resultado_real]               | [estado] |

## Módulo: Productos (CRUD)

| ID     | Descripción                          | Precondición               | Pasos                                                        | Resultado esperado                     | Resultado real                     | Estado   |
| ------ | ------------------------------------ | -------------------------- | ------------------------------------------------------------ | -------------------------------------- | ---------------------------------- | -------- |
| CP-005 | Crear producto válido                | Sesión iniciada            | 1. Abrir módulo Productos 2. Completar formulario 3. Guardar | Producto registrado y visible en tabla | Producto creado correctamente      | Paso     |
| CP-006 | Crear producto con datos incompletos | Sesión iniciada            | 1. Abrir formulario 2. Omitir descripción 3. Guardar         | Sistema valida y no registra           | [resultado_real]                   | [estado] |
| CP-007 | Editar producto existente            | Existe producto registrado | 1. Seleccionar producto 2. Editar descripción 3. Guardar     | Cambios visibles en listado            | Producto actualizado correctamente | Paso     |
| CP-008 | Eliminar producto existente          | Existe producto registrado | 1. Seleccionar producto 2. Eliminar 3. Confirmar             | Registro eliminado del listado         | Producto eliminado correctamente   | Paso     |

## Módulo: Pedidos (Orders)

| ID     | Descripción                       | Precondición                             | Pasos                                                                                               | Resultado esperado                                     | Resultado real                  | Estado   |
| ------ | --------------------------------- | ---------------------------------------- | --------------------------------------------------------------------------------------------------- | ------------------------------------------------------ | ------------------------------- | -------- |
| CP-009 | Registrar pedido válido           | Usuario autenticado y productos cargados | 1. Abrir /orders 2. Seleccionar producto 3. Ingresar descripción 4. Seleccionar estado 5. Registrar | Aparece alerta "Pedido registrado" y se almacena en BD | Pedido registrado correctamente | Paso     |
| CP-010 | Registrar pedido sin descripción  | Usuario autenticado                      | 1. Abrir /orders 2. No ingresar descripción 3. Registrar                                            | Validación HTML impide envío                           | [resultado_real]                | [estado] |
| CP-011 | Registrar pedido sin producto     | Usuario autenticado                      | 1. Abrir /orders 2. No seleccionar producto 3. Registrar                                            | Sistema impide registro                                | [resultado_real]                | [estado] |
| CP-012 | Verificar pedido registrado en BD | Pedido CP-009 ejecutado                  | 1. Abrir SQLite 2. Consultar tabla orders 3. Verificar registro                                     | Registro almacenado correctamente                      | Registro encontrado en BD       | Paso     |

## Evidencias Asociadas

| Caso   | Evidencia                    |
| ------ | ---------------------------- |
| CP-001 | CP-001-login-exitoso.png     |
| CP-002 | CP-002-login-fallido.png     |
| CP-005 | CP-003-crear-producto.png    |
| CP-007 | CP-004-editar-producto.png   |
| CP-008 | CP-005-eliminar-producto.png |
| CP-009 | CP-006-pedido-valido.png     |
| CP-010 | CP-007-pedido-invalido.png   |

## Herramienta utilizada

* Selenium IDE
* Google Chrome
* Ambiente Local
* URL Base: http://localhost:8080
