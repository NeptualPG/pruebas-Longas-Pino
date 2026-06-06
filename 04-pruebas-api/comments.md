# Fase 4 - Pruebas API

## Objetivo

Validar el correcto funcionamiento de los servicios REST del sistema mediante pruebas automatizadas y manuales utilizando Postman.

## Herramienta utilizada

* Postman
* Colección: `Jeanstyle-PruebasAPI`
* Ambiente: Local
* URL Base: `http://localhost:8080`

## Módulos evaluados

### 1. Login

Endpoints evaluados:

```http
POST /login
```

Casos ejecutados:

* Login exitoso.
* Login con credenciales inválidas.
* Login con datos incompletos.

Resultado:

Las validaciones de autenticación respondieron conforme a los escenarios definidos.

---

### 2. Maestro (Productos)

Endpoints evaluados:

```http
GET    /api/productos
GET    /api/productos/{id}
POST   /api/productos
PUT    /api/productos/{id}
DELETE /api/productos/{id}
```

Casos ejecutados:

* Listar productos.
* Consultar producto por ID.
* Crear producto válido.
* Crear producto inválido.
* Editar producto existente.
* Eliminar producto.

Resultado:

Las operaciones CRUD fueron ejecutadas correctamente sobre la entidad producto.

---

### 3. Transaccional (Pedidos)

Endpoints evaluados:

```http
POST /api/orders
```

Casos ejecutados:

* Registrar pedido válido.
* Registrar pedido inválido.

Resultado:

Las reglas de validación y registro de pedidos fueron verificadas satisfactoriamente.

---

## Evidencias

### Evidencia 1

Archivo:

```text
evidencias/api-login-ok.png
```

Descripción:

Ejecución exitosa del endpoint de autenticación.

### Evidencia 2

Archivo:

```text
evidencias/api-productos-crud.png
```

Descripción:

Pruebas CRUD realizadas sobre el módulo maestro de productos.

### Evidencia 3

Archivo:

```text
evidencias/api-orders.png
```

Descripción:

Registro de pedidos mediante endpoint transaccional.

### Evidencia 4

Archivo:

```text
evidencias/postman-tests.png
```

Descripción:

Resultado de ejecución de pruebas automáticas y validaciones Postman.

---

## Validaciones realizadas

| Caso                      | Resultado |
| ------------------------- | --------- |
| Login exitoso             | Aprobado  |
| Login inválido            | Aprobado  |
| Listar productos          | Aprobado  |
| Crear producto            | Aprobado  |
| Editar producto           | Aprobado  |
| Eliminar producto         | Aprobado  |
| Registrar pedido válido   | Aprobado  |
| Registrar pedido inválido | Aprobado  |

---

## Colección utilizada

Archivos:

```text
Jeanstyle-PruebasAPI.postman_collection.json
env-local-pruebas.postman_environment.json
```

## Conclusión

Se ejecutaron satisfactoriamente las pruebas API definidas para los módulos de autenticación, maestro y transaccional. Los endpoints respondieron de acuerdo con los criterios funcionales establecidos y las validaciones implementadas permitieron verificar el comportamiento esperado del sistema.
