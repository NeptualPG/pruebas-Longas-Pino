# Criterios de Aceptación - Jeanstyle

## Módulo Login

### CA-001

**Dado** un usuario registrado y habilitado en la tabla `users`,
**Cuando** ingresa credenciales válidas en `/login`,
**Entonces** el sistema permite el acceso y crea una sesión activa.

### CA-002

**Dado** un usuario registrado,
**Cuando** ingresa una contraseña incorrecta,
**Entonces** el sistema rechaza el acceso y muestra un mensaje de error.

### CA-003

**Dado** un usuario inexistente,
**Cuando** intenta iniciar sesión,
**Entonces** el sistema rechaza la autenticación sin revelar información sensible.

### CA-004

**Dado** el formulario de login,
**Cuando** los campos obligatorios están vacíos,
**Entonces** el sistema impide el envío y muestra validaciones.

### CA-005

**Dado** un usuario deshabilitado (`enabled = 0`),
**Cuando** intenta iniciar sesión,
**Entonces** el sistema deniega el acceso.

### CA-006

**Dado** una sesión válida,
**Cuando** el usuario accede al Dashboard,
**Entonces** el sistema muestra únicamente la información asociada a su cuenta.

### CA-007

**Dado** un usuario autenticado,
**Cuando** cierra sesión,
**Entonces** el sistema invalida la sesión activa.

---

## Módulo Productos (CRUD)

### CA-008

**Dado** un usuario autenticado,
**Cuando** registra un nuevo producto con datos válidos,
**Entonces** el sistema almacena el registro en la tabla `producto`.

### CA-009

**Dado** un producto existente,
**Cuando** se consulta mediante el listado de productos,
**Entonces** el sistema muestra la información completa del registro.

### CA-010

**Dado** un producto existente,
**Cuando** se modifica su descripción o atributos,
**Entonces** el sistema actualiza correctamente los datos.

### CA-011

**Dado** un producto existente,
**Cuando** se elimina desde el módulo de productos,
**Entonces** el sistema elimina el registro y deja de mostrarlo en el listado.

### CA-012

**Dado** un formulario de producto,
**Cuando** faltan campos obligatorios,
**Entonces** el sistema impide guardar el registro.

### CA-013

**Dado** una consulta de productos,
**Cuando** existen registros en la base de datos,
**Entonces** el sistema retorna todos los productos disponibles.

### CA-014

**Dado** un producto registrado,
**Cuando** se consulta directamente en la base de datos,
**Entonces** la información coincide con la mostrada en la interfaz.

---

## Módulo Pedidos (Orders)

### CA-015

**Dado** un usuario autenticado y un producto existente,
**Cuando** registra un pedido válido,
**Entonces** el sistema crea un registro en la tabla `orders`.

### CA-016

**Dado** un formulario de pedidos,
**Cuando** el usuario deja vacíos los campos obligatorios,
**Entonces** el sistema impide registrar el pedido.

### CA-017

**Dado** un pedido registrado,
**Cuando** se consulta el listado de pedidos,
**Entonces** el sistema muestra la información almacenada.

### CA-018

**Dado** un pedido válido,
**Cuando** el registro se almacena correctamente,
**Entonces** el sistema genera un identificador único para el pedido.

### CA-019

**Dado** un pedido registrado,
**Cuando** se consulta directamente en la tabla `orders`,
**Entonces** los datos coinciden con los mostrados en la interfaz.

### CA-020

**Dado** un usuario sin sesión activa,
**Cuando** intenta acceder directamente al módulo de pedidos,
**Entonces** el sistema redirige al login o deniega el acceso.

---

## Cobertura de Validación

| Módulo    | Criterios       |
| --------- | --------------- |
| Login     | CA-001 a CA-007 |
| Productos | CA-008 a CA-014 |
| Pedidos   | CA-015 a CA-020 |

**Total:** 20 criterios de aceptación.
