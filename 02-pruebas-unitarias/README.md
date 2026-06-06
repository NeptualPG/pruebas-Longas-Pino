# Fase 2: Pruebas Unitarias - Jeanstyle

## Descripción

Pruebas unitarias ejecutadas sobre las funcionalidades principales implementadas en el sistema Jeanstyle.

Se validan:

* Inicio de sesión de usuarios.
* Gestión de productos (CRUD).
* Gestión de pedidos (Orders).
* Integridad básica de operaciones sobre la base de datos.

---

## Estructura

```text
02-pruebas-unitarias/
├── tests/
│   ├── test_auth.py
│   ├── test_productos.py
│   └── test_orders.py
│
├── evidencias/
│   ├── test_report.html
│   ├── coverage_report.html
│   └── consola-ejecucion.png
│
├── requirements.txt
└── README.md
```

---

## Pruebas Incluidas

### 1. TestLoginExitoso

**Objetivo**

Validar autenticación correcta de usuario registrado.

**Validaciones**

* Usuario existe.
* Contraseña correcta.
* Login exitoso.
* Se crea sesión válida.

---

### 2. TestPasswordIncorrecta

**Objetivo**

Validar rechazo de credenciales inválidas.

**Validaciones**

* Login rechazado.
* Mensaje de error.
* No se crea sesión.

---

### 3. TestCrearProducto

**Objetivo**

Validar creación de productos.

**Validaciones**

* Registro insertado correctamente.
* ID generado.
* Persistencia en base de datos.

---

### 4. TestEditarProducto

**Objetivo**

Validar actualización de productos.

**Validaciones**

* Modificación exitosa.
* Datos actualizados en consulta posterior.

---

### 5. TestEliminarProducto

**Objetivo**

Validar eliminación de productos.

**Validaciones**

* Registro eliminado.
* No aparece en listados posteriores.

---

### 6. TestCrearPedido

**Objetivo**

Validar creación de pedidos.

**Validaciones**

* Pedido insertado.
* Relación con producto válida.
* Estado almacenado correctamente.

---

### 7. TestPedidoInvalido

**Objetivo**

Validar restricciones de negocio.

**Validaciones**

* No permite registrar pedidos incompletos.
* Retorna error controlado.

---

## Instalación de Dependencias

```bash
conda activate python312

pip install pytest
pip install pytest-html
pip install pytest-cov
```

---

## Ejecución

### Ejecutar todas las pruebas

```bash
pytest -v
```

### Ejecutar autenticación

```bash
pytest tests/test_auth.py -v
```

### Ejecutar productos

```bash
pytest tests/test_productos.py -v
```

### Ejecutar pedidos

```bash
pytest tests/test_orders.py -v
```

### Ejecutar con cobertura

```bash
pytest --cov=. --cov-report=html
```

---

## Requisitos Previos

### Base de datos creada

```bash
python db/init_db.py
```

### Validar tablas principales

```bash
sqlite3 db/database.sqlite ".tables"
```

Resultado esperado:

```text
users
producto
orders
prenda
molde
tela
estilo
estados
usuario
```

### Verificar integridad

```bash
sqlite3 db/database.sqlite "PRAGMA integrity_check;"
```

Resultado esperado:

```text
ok
```

---

## Datos de Prueba

### Usuario

```text
Correo: stayconnectpg@gmail.com
Contraseña: YuLL&71T87N-
```

### Producto

```text
Descripción: Camiseta personalizada básica
Estado: Activo
Talla: M
```

### Pedido

```text
Producto: Camiseta personalizada básica
Estado: En proceso
Descripción: Pedido de prueba
```

---

## Reportes

Los resultados de ejecución se almacenan en:

```text
evidencias/test_report.html
evidencias/coverage_report.html
```

---

## Resultado Esperado

```text
=====================
7 PASSED
=====================
```

---

## Relación con las demás fases

| Fase   | Descripción         |
| ------ | ------------------- |
| Fase 2 | Pruebas Unitarias   |
| Fase 3 | Selenium IDE        |
| Fase 4 | API Postman         |
| Fase 5 | Base de Datos       |
| Fase 6 | Seguridad OWASP ZAP |

---

**Proyecto:** Jeanstyle
**Versión:** 1.1
**Ambiente:** Local
**Herramienta:** Pytest + SQLite
