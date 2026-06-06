# ESTADO DEL PROYECTO - JEANSTYLE

## Actualización Final - Junio 2026

## Resumen Ejecutivo

El proyecto de pruebas se encuentra prácticamente finalizado.

Las seis fases definidas en la guía cuentan con documentación, evidencias y artefactos asociados. Durante el desarrollo se realizaron ajustes sobre la base de datos SQLite, los módulos CRUD de productos y el módulo transaccional de pedidos (Orders).

Actualmente el proyecto se encuentra en etapa de consolidación de evidencias y revisión final de documentación.

---

# Estado por Fases

| Fase                         | Estado     | Progreso |
| ---------------------------- | ---------- | -------- |
| Fase 1 - Planificación       | Completada | 100%     |
| Fase 2 - Pruebas Unitarias   | Completada | 100%     |
| Fase 3 - Pruebas Funcionales | Completada | 100%     |
| Fase 4 - Pruebas API         | Completada | 100%     |
| Fase 5 - Base de Datos       | Completada | 100%     |
| Fase 6 - Seguridad           | Completada | 100%     |

**Avance General:** 100%

---

# Fase 1 - Planificación

## Entregables

### Plan de Pruebas

* Alcance definido.
* Estrategia de pruebas documentada.
* Herramientas identificadas.
* Riesgos identificados.

### Criterios de Aceptación

* Casos de Login.
* Casos CRUD Productos.
* Casos Pedidos.
* Casos API.
* Casos Base de Datos.

## Estado

✅ Completado

---

# Fase 2 - Pruebas Unitarias

## Artefactos

```text
02-pruebas-unitarias/
```

### Implementado

* test_auth.py
* test_productos.py
* test_orders.py

### Validaciones

* Login correcto.
* Login incorrecto.
* Creación de productos.
* Edición de productos.
* Eliminación de productos.
* Registro de pedidos.
* Validaciones de negocio.

### Evidencias

* Reporte Pytest.
* Captura de ejecución.
* Evidencias HTML.

## Estado

✅ Completado

---

# Fase 3 - Pruebas Funcionales

## Herramienta

* Selenium IDE

## Casos ejecutados

### Login

* CP-001 Login exitoso
* CP-002 Login fallido

### Productos

* CP-003 Crear producto
* CP-004 Editar producto
* CP-005 Eliminar producto

### Pedidos

* CP-006 Pedido válido
* CP-007 Pedido inválido

## Evidencias

```text
03-pruebas-funcionales/evidencias/
```

* Capturas de Selenium.
* Suite Selenium IDE.
* Evidencia de ejecución exitosa.

## Estado

✅ Completado

---

# Fase 4 - Pruebas API

## Herramienta

* Postman

## Módulos cubiertos

### Login

* Login válido.
* Login inválido.

### Productos

* Listar.
* Crear.
* Actualizar.
* Eliminar.

### Orders

* Crear pedido.
* Validaciones.

## Evidencias

```text
04-pruebas-api/
```

* Colección Postman.
* Environment.
* Capturas de ejecución.

## Estado

✅ Completado

---

# Fase 5 - Pruebas Base de Datos

## Herramienta

* SQLite

## Validaciones realizadas

### Integridad

```sql
PRAGMA integrity_check;
```

Resultado:

```text
ok
```

### Relaciones

* producto → prenda
* producto → molde
* producto → tela
* producto → estilo
* producto → usuario
* producto → estados

### Inserciones de prueba

* Productos.
* Pedidos.
* Usuarios.

## Evidencias

```text
05-base-de-datos/
```

* Scripts SQL.
* Capturas SQLiteStudio.
* Resultados consultas.

## Estado

✅ Completado

---

# Fase 6 - Seguridad

## Herramienta

* OWASP ZAP

## Actividades

* Escaneo automatizado.
* Revisión de alertas.
* Exportación de reporte HTML.

## Evidencias

```text
06-seguridad/
```

* reporte-zap.html
* Capturas de escaneo.
* Tabla de hallazgos.

## Estado

✅ Completado

---

# Problemas Encontrados Durante el Proyecto

## Base de Datos SQLite

### Incidentes resueltos

* database disk image is malformed
* no such table users
* no such column p.id_talla
* no such column o.descripcion
* database is locked

### Solución

* Recreación de estructura.
* Ajuste de columnas.
* Actualización de consultas SQL.
* Carga de datos de prueba.

---

# Herramientas Utilizadas

* Python 3.12
* SQLite
* Selenium IDE
* Postman
* OWASP ZAP
* VS Code
* Git

---

# Conclusión

El proyecto Jeanstyle cuenta con evidencias funcionales, unitarias, API, base de datos y seguridad.

Todos los entregables definidos en la guía fueron desarrollados y organizados por fases, quedando listo para revisión académica y sustentación.
