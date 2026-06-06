# Fase 5 - Pruebas de Base de Datos

## Objetivo

Validar la integridad de los datos, las restricciones de la base de datos y el comportamiento transaccional del sistema.

## Base de datos evaluada

* Motor: SQLite
* Archivo: `db/database1.sqlite`
* Ambiente: Local

## Scripts ejecutados

### 1. Datos de prueba

Archivo:

```text
datos-prueba.sql
```

Objetivo:

Validar la existencia de registros de prueba en las tablas principales del sistema.

Tablas verificadas:

* producto
* usuario
* prenda
* estilo
* tela
* estados
* orders

---

### 2. Pruebas de integridad

Archivo:

```text
pruebas-integridad.sql
```

Objetivo:

Validar la consistencia de las claves foráneas y relaciones entre tablas.

Consulta ejecutada:

```sql
PRAGMA foreign_key_check;
```

Resultado obtenido:

Se detectó una inconsistencia de integridad referencial.

Detalle:

```text
foreign key mismatch - "password_reset_tokens" referencing "users"
```

Análisis:

La tabla `password_reset_tokens` referencia la columna:

```text
users.id
```

Sin embargo, la clave primaria existente en la tabla `users` corresponde a:

```text
users.id_usuario
```

Por lo tanto, la definición de la clave foránea presenta una inconsistencia estructural.

---

### 3. Pruebas de transacciones

Archivo:

```text
pruebas-transacciones.sql
```

Objetivo:

Verificar el comportamiento de las operaciones COMMIT y ROLLBACK.

Prueba realizada:

* Inicio de transacción.
* Intento de inserción de registros.
* Validación de restricciones.
* Reversión de cambios mediante ROLLBACK.

Resultado obtenido:

La base de datos impidió la inserción de registros con referencias inválidas mediante restricciones de clave foránea.

Mensaje obtenido:

```text
FOREIGN KEY constraint failed
```

Interpretación:

Las restricciones de integridad referencial se encuentran activas y funcionando correctamente, evitando la inserción de datos inconsistentes.

---

## Evidencias

### Evidencia 1

Archivo:

```text
evidencias/datos-prueba.png
```

Descripción:

Consulta y visualización de registros existentes en las tablas principales.

### Evidencia 2

Archivo:

```text
evidencias/integridad-fk-check.png
```

Descripción:

Resultado de la validación de claves foráneas mediante `PRAGMA foreign_key_check`.

### Evidencia 3

Archivo:

```text
evidencias/integridad-users-structure.png
```

Descripción:

Estructura de la tabla `users` utilizada para identificar la inconsistencia detectada.

### Evidencia 4

Archivo:

```text
evidencias/transacciones.png
```

Descripción:

Resultado de las pruebas de transacciones y validación de restricciones de integridad.

---

## Hallazgos

| ID     | Hallazgo                                                        | Severidad   |
| ------ | --------------------------------------------------------------- | ----------- |
| BD-001 | Clave foránea inconsistente entre password_reset_tokens y users | Media       |
| BD-002 | Restricciones FK impiden inserciones inválidas correctamente    | Informativo |

---

## Conclusión

Se ejecutaron satisfactoriamente las pruebas de base de datos definidas para la iteración. Se verificó la existencia de datos de prueba, la integridad referencial y el comportamiento transaccional del sistema. Se identificó una inconsistencia en una clave foránea relacionada con la tabla `password_reset_tokens`, la cual deberá ser corregida para garantizar la consistencia total del modelo de datos.
