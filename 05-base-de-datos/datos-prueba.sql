-- Script 1: datos-prueba.sql
-- Proposito: insertar datos controlados y reproducibles.

-- Paso 1: seleccionar base de datos
USE [nombre_base_de_datos];

-- Paso 2: verificar estructura real
SHOW TABLES;
DESCRIBE [tabla_usuarios];
DESCRIBE [tabla_maestra];
DESCRIBE [tabla_transaccional];

-- Paso 3: limpiar datos de pruebas previas
DELETE FROM [tabla_transaccional] WHERE [campo_descripcion] LIKE 'PRUEBA_%';
DELETE FROM [tabla_maestra] WHERE [campo_codigo] LIKE 'TEST_%';
DELETE FROM [tabla_usuarios] WHERE [campo_usuario] LIKE 'test_%';

-- Paso 4: insertar usuarios de prueba
INSERT INTO [tabla_usuarios]
([campo_usuario], [campo_password], [campo_nombre], [campo_rol], [campo_activo])
VALUES
('test_admin', [func_hash]('[clave_admin]'), '[nombre_admin_prueba]', '[rol_admin]', 1),
('test_user', [func_hash]('[clave_user]'), '[nombre_user_prueba]', '[rol_user]', 1),
('test_inactivo', [func_hash]('[clave_inactiva]'), '[nombre_inactivo_prueba]', '[rol_user]', 0);

SELECT [campo_usuario], [campo_nombre], [campo_rol], [campo_activo]
FROM [tabla_usuarios]
WHERE [campo_usuario] LIKE 'test_%';

-- Paso 5: insertar registros maestros
INSERT INTO [tabla_maestra]
([campo_codigo], [campo_nombre], [campo_descripcion], [campo_activo])
VALUES
('TEST_001', '[nombre_registro_1]', '[descripcion_1]', 1),
('TEST_002', '[nombre_registro_2]', '[descripcion_2]', 1),
('TEST_003', '[nombre_registro_3]', '[descripcion_3]', 1);

SELECT * FROM [tabla_maestra] WHERE [campo_codigo] LIKE 'TEST_%';

-- Paso 6: insertar transacciones de prueba
INSERT INTO [tabla_transaccional]
([campo_id_usuario], [campo_id_maestro], [campo_descripcion], [campo_monto], [campo_fecha], [campo_estado])
VALUES
([id_usuario_1], [id_maestro_1], 'PRUEBA_TRX_001', [monto_1], NOW(), '[estado_completada]'),
([id_usuario_1], [id_maestro_2], 'PRUEBA_TRX_002', [monto_2], NOW(), '[estado_completada]'),
([id_usuario_2], [id_maestro_1], 'PRUEBA_TRX_003', [monto_3], NOW(), '[estado_pendiente]');

SELECT * FROM [tabla_transaccional] WHERE [campo_descripcion] LIKE 'PRUEBA_%';
