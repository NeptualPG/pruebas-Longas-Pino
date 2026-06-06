# Plan de Pruebas - Jeanstyle

## 1. Información General

* Sistema: Jeanstyle
* Versión bajo prueba: 1.0
* Ambiente objetivo: Local
* Responsable QA: Diego Pino - Juan Longas
* Fecha: Junio 2026

### Descripción

Jeanstyle es una aplicación web para la gestión de productos textiles y pedidos de clientes. El sistema permite autenticación de usuarios, administración de productos y registro de pedidos, utilizando una base de datos SQLite y una arquitectura basada en Python.

---

## 2. Módulos en Alcance

### Incluidos

1. Login
2. Gestión de Productos (CRUD)
3. Gestión de Pedidos (Orders)

### Fuera de Alcance

* Integraciones de pago externas.
* Servicios de correo SMTP en producción.

---

## 3. Objetivos de Prueba

* Validar autenticación y acceso al sistema.
* Validar operaciones CRUD de productos.
* Validar registro y consulta de pedidos.
* Verificar integridad de datos en SQLite.
* Validar funcionamiento de los endpoints API.
* Identificar vulnerabilidades básicas mediante análisis de seguridad.

---

## 4. Tipos de Prueba

* Pruebas Unitarias (Pytest)
* Pruebas Funcionales (Selenium IDE)
* Pruebas API (Postman)
* Pruebas de Base de Datos (SQLite)
* Pruebas de Seguridad (OWASP ZAP)

---

## 5. Matriz Módulo vs Tipo de Prueba

| Módulo    | Unitarias | Funcionales | API | BD | Seguridad |
| --------- | --------- | ----------- | --- | -- | --------- |
| Login     | Sí        | Sí          | Sí  | Sí | Sí        |
| Productos | Sí        | Sí          | Sí  | Sí | Sí        |
| Pedidos   | Sí        | Sí          | Sí  | Sí | Sí        |

---

## 6. Criterios de Entrada

* Aplicación desplegada en entorno local.
* Base de datos SQLite creada.
* Tablas principales inicializadas.
* Usuario de prueba disponible.
* Datos de prueba cargados.
* Endpoints accesibles desde navegador y Postman.

---

## 7. Criterios de Salida

* Casos de prueba ejecutados al 100%.
* Evidencias almacenadas por fase.
* Resultados documentados.
* Reporte final consolidado.
* Vulnerabilidades registradas y analizadas.

---

## 8. Riesgos y Mitigación

| Riesgo                             | Impacto | Probabilidad | Mitigación                                 |
| ---------------------------------- | ------- | ------------ | ------------------------------------------ |
| Corrupción de base de datos SQLite | Alto    | Media        | Respaldo previo y recreación de estructura |
| Cambios de esquema durante pruebas | Alto    | Media        | Validar estructura antes de ejecutar       |
| Datos de prueba insuficientes      | Medio   | Media        | Scripts de carga de datos                  |
| Errores de configuración local     | Medio   | Media        | Validación previa del ambiente             |
| Bloqueos SQLite (database locked)  | Medio   | Media        | Cierre adecuado de conexiones              |

---

## 9. Cronograma

| Fase | Actividad                               | Duración |
| ---- | --------------------------------------- | -------- |
| 1    | Planificación y criterios de aceptación | 3 horas  |
| 2    | Pruebas unitarias                       | 5 horas  |
| 3    | Pruebas funcionales                     | 5 horas  |
| 4    | Pruebas API                             | 4 horas  |
| 5    | Pruebas de base de datos                | 4 horas  |
| 6    | Pruebas de seguridad                    | 2 horas  |
| 7    | Consolidación y entrega final           | 2 horas  |

**Total:** 25 horas

---

## 10. Herramientas

| Herramienta  | Uso                  |
| ------------ | -------------------- |
| VS Code      | Desarrollo           |
| Python 3.12  | Backend              |
| Pytest       | Pruebas unitarias    |
| Selenium IDE | Pruebas funcionales  |
| Postman      | Pruebas API          |
| SQLiteStudio | Base de datos        |
| OWASP ZAP    | Seguridad            |
| Git          | Control de versiones |

---

## 11. Entregables

### Fase 1

* Plan de pruebas.
* Criterios de aceptación.

### Fase 2

* Scripts de pruebas unitarias.
* Reportes de ejecución.

### Fase 3

* Selenium Suite.
* Casos funcionales.
* Evidencias de ejecución.

### Fase 4

* Colección Postman.
* Environment Postman.
* Evidencias API.

### Fase 5

* Scripts SQL.
* Evidencias de integridad.
* Evidencias de transacciones.

### Fase 6

* Reporte OWASP ZAP.
* Evidencias de seguridad.

### Entrega Final

* Reporte consolidado.
* Evidencias organizadas por fase.
* Video de sustentación.
