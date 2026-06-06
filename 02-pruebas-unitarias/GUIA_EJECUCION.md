# GUÍA DE EJECUCIÓN - Fase 2: Pruebas Unitarias

## Resumen

Esta fase ejecuta pruebas unitarias sobre las funcionalidades principales implementadas en el sistema Jeanstyle:

* Autenticación de usuarios
* Gestión de productos
* Gestión de pedidos (Orders)

Las pruebas se ejecutan utilizando Pytest sobre las funciones del proyecto.

---

## Inicio Rápido

### Activar entorno

```powershell
conda activate python312
```

### Instalar dependencias

```powershell
pip install pytest pytest-html pytest-cov
```

### Ejecutar todas las pruebas

```powershell
pytest -v
```

### Ejecutar únicamente autenticación

```powershell
pytest tests/test_auth.py -v
```

### Ejecutar únicamente productos

```powershell
pytest tests/test_productos.py -v
```

### Ejecutar únicamente pedidos

```powershell
pytest tests/test_orders.py -v
```

---

## Casos Unitarios Cubiertos

### UT-001 Login exitoso

**Objetivo**

Validar que un usuario registrado pueda autenticarse correctamente.

**Datos**

```text
Correo: stayconnectpg@gmail.com
Password: YuLL&71T87N-
```

**Resultado esperado**

* Login exitoso.
* Retorna sesión válida.
* Usuario autenticado.

---

### UT-002 Login fallido

**Objetivo**

Validar rechazo de contraseña incorrecta.

**Resultado esperado**

* Login rechazado.
* Mensaje de error.
* No genera sesión.

---

### UT-003 Crear producto

**Objetivo**

Validar inserción correcta en tabla producto.

**Resultado esperado**

* Registro creado.
* ID generado.
* Datos almacenados correctamente.

---

### UT-004 Actualizar producto

**Objetivo**

Validar modificación de producto existente.

**Resultado esperado**

* Registro actualizado.
* Datos reflejados en consulta posterior.

---

### UT-005 Eliminar producto

**Objetivo**

Validar eliminación lógica o física de producto.

**Resultado esperado**

* Producto eliminado.
* No aparece en listados.

---

### UT-006 Crear pedido

**Objetivo**

Validar inserción de pedidos en tabla orders.

**Resultado esperado**

* Pedido registrado.
* Estado almacenado.
* Relación con producto válida.

---

### UT-007 Validación de pedido inválido

**Objetivo**

Validar rechazo cuando faltan datos obligatorios.

**Resultado esperado**

* No se crea pedido.
* Se retorna mensaje de validación.

---

## Evidencias Generadas

Después de ejecutar:

```powershell
pytest -v --html=evidencias/test_report.html --self-contained-html
```

se generan:

```text
02-pruebas-unitarias/
│
├── evidencias/
│   ├── test_report.html
│   ├── cobertura.html
│   └── consola-ejecucion.png
│
├── tests/
│   ├── test_auth.py
│   ├── test_productos.py
│   └── test_orders.py
│
└── README.md
```

---

## Resultado Esperado

```text
=========================
7 passed in 0.85s
=========================
```

---

## Verificaciones Previas

### Base de datos

```powershell
sqlite3 db/database.sqlite ".tables"
```

Debe mostrar:

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

### Integridad

```powershell
sqlite3 db/database.sqlite "PRAGMA integrity_check;"
```

Resultado esperado:

```text
ok
```

### Usuario de prueba

```sql
SELECT correo
FROM users
WHERE correo='stayconnectpg@gmail.com';
```

Resultado esperado:

```text
stayconnectpg@gmail.com
```

---

## Evidencia requerida

* Captura ejecución Pytest exitosa.
* Reporte HTML generado.
* Evidencia de cobertura (opcional).
* Captura de consola mostrando pruebas exitosas.

## Herramientas

* Python 3.12
* Pytest
* SQLite
* VS Code
* PowerShell

## Estado esperado de la fase

**APROBADA** cuando todas las pruebas unitarias ejecuten correctamente y el reporte indique:

```text
PASSED
```
