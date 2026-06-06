# pruebas-pino-longas

Repositorio de evidencias y ejecución de pruebas de software realizadas sobre el proyecto web **Jeanstyle**, siguiendo una estrategia de validación por fases.

## Módulos evaluados

1. Login
2. Gestión de Productos (CRUD)
3. Gestión de Pedidos (Orders)

---

# Tabla de Contenido

1. Descripción General
2. Herramientas Utilizadas
3. Estructura del Repositorio
4. Fase 1 - Planificación
5. Fase 2 - Pruebas Unitarias
6. Fase 3 - Pruebas Funcionales
7. Fase 4 - Pruebas API
8. Fase 5 - Pruebas de Base de Datos
9. Fase 6 - Pruebas de Seguridad
10. Casos de Prueba
11. Reporte de Bugs
12. Evidencias
13. Checklist Final

---

# 1. Descripción General

El objetivo del proyecto fue planificar, ejecutar y documentar pruebas de software sobre la aplicación Jeanstyle utilizando herramientas de pruebas funcionales, unitarias, API, base de datos y seguridad.

Las actividades se organizaron en seis fases independientes para facilitar la trazabilidad de los resultados.

---

# 2. Herramientas Utilizadas

| Herramienta           | Uso                      |
| --------------------- | ------------------------ |
| Pytest                | Pruebas Unitarias        |
| Selenium IDE          | Pruebas Funcionales      |
| Postman               | Pruebas API              |
| SQLite / SQLiteStudio | Validación Base de Datos |
| OWASP ZAP             | Seguridad                |
| VS Code               | Desarrollo               |
| Git                   | Control de Versiones     |

---

# 3. Estructura del Repositorio

```text
01-planificacion/
02-pruebas-unitarias/
03-pruebas-funcionales/
04-pruebas-api/
05-base-de-datos/
06-seguridad/
07-entrega-final/
```

---

# 4. Fase 1 - Planificación

## Entregables

* plan-de-pruebas.md
* criterios-aceptacion.md

## Resultado

Se definieron los criterios de aceptación para:

* Login
* Productos
* Pedidos

Estado:

✅ Completada

---

# 5. Fase 2 - Pruebas Unitarias

## Casos cubiertos

### Autenticación

* Login exitoso
* Login inválido

### Productos

* Crear producto
* Editar producto
* Eliminar producto

### Pedidos

* Crear pedido
* Validar pedido inválido

## Herramienta

Pytest

## Evidencias

```text
02-pruebas-unitarias/evidencias/
```

Estado:

✅ Completada

---

# 6. Fase 3 - Pruebas Funcionales

## Herramienta

Selenium IDE

## Casos ejecutados

| Código | Caso              |
| ------ | ----------------- |
| CP-001 | Login exitoso     |
| CP-002 | Login fallido     |
| CP-003 | Crear producto    |
| CP-004 | Editar producto   |
| CP-005 | Eliminar producto |
| CP-006 | Pedido válido     |
| CP-007 | Pedido inválido   |

## Evidencias

```text
03-pruebas-funcionales/evidencias/
```

Estado:

✅ Completada

---

# 7. Fase 4 - Pruebas API

## Herramienta

Postman

## Operaciones validadas

### Productos

* GET
* POST
* PUT
* DELETE

### Orders

* POST
* Validaciones

## Archivos

```text
04-pruebas-api/
├── coleccion-postman.json
└── environment-postman.json
```

Estado:

✅ Completada

---

# 8. Fase 5 - Pruebas Base de Datos

## Herramienta

SQLite

## Actividades realizadas

* Inserción de datos de prueba.
* Validación de claves foráneas.
* Verificación de integridad.
* Validación de pedidos y productos.

## Evidencias

```text
05-base-de-datos/
```

Estado:

✅ Completada

---

# 9. Fase 6 - Pruebas de Seguridad

## Herramienta

OWASP ZAP

## Actividades

* Escaneo automatizado.
* Revisión de alertas.
* Exportación de reporte HTML.

## Archivos

```text
06-seguridad/
├── reporte-zap.html
└── evidencias/
```

Estado:

✅ Completada

---

# 10. Casos de Prueba

Los casos funcionales se encuentran en:

```text
03-pruebas-funcionales/casos-prueba-funcionales.md
```

Incluyen:

* Resultado esperado.
* Resultado real.
* Estado de ejecución.

---

# 11. Reporte de Bugs

Los defectos encontrados durante el proyecto se documentan en:

```text
07-entrega-final/reporte-bugs.md
```

Ejemplos encontrados:

* database disk image is malformed
* no such table users
* no such column p.id_talla
* no such column o.descripcion
* database is locked

---

# 12. Evidencias

Todas las evidencias incluyen:

* Capturas de pantalla.
* Reportes HTML.
* Consultas SQL.
* Ejecuciones Selenium.
* Resultados Postman.
* Reporte OWASP ZAP.

---

# 13. Checklist Final

* [x] Plan de pruebas.
* [x] Criterios de aceptación.
* [x] Pruebas unitarias.
* [x] Pruebas funcionales.
* [x] Pruebas API.
* [x] Pruebas base de datos.
* [x] Pruebas de seguridad.
* [x] Evidencias organizadas.
* [x] Reporte final.

---

## Estado Final del Proyecto

**Proyecto:** Jeanstyle

**Estado:** Finalizado

**Resultado:** Entrega lista para evaluación académica.
