-- Script 3: pruebas-transacciones.sql
-- Proposito: validar atomicidad y consistencia de COMMIT/ROLLBACK.

-- Paso 1: transaccion exitosa (COMMIT)
SELECT COUNT(*) AS total_antes FROM [tabla_transaccional];

START TRANSACTION;

INSERT INTO [tabla_transaccional]
([campo_id_usuario], [campo_id_maestro], [campo_descripcion], [campo_monto], [campo_fecha], [campo_estado])
VALUES
([id_usuario_1], [id_maestro_1], 'PRUEBA_COMMIT', [monto_commit], NOW(), '[estado_completada]');

SELECT * FROM [tabla_transaccional]
WHERE [campo_descripcion] = 'PRUEBA_COMMIT';

COMMIT;

SELECT COUNT(*) AS total_despues FROM [tabla_transaccional];

SELECT * FROM [tabla_transaccional]
WHERE [campo_descripcion] = 'PRUEBA_COMMIT';
-- Esperado: 1 fila

-- Paso 2: transaccion revertida (ROLLBACK)
SELECT COUNT(*) AS total_antes FROM [tabla_transaccional];

START TRANSACTION;

INSERT INTO [tabla_transaccional]
([campo_id_usuario], [campo_id_maestro], [campo_descripcion], [campo_monto], [campo_fecha], [campo_estado])
VALUES
([id_usuario_1], [id_maestro_1], 'PRUEBA_ROLLBACK', [monto_rollback], NOW(), '[estado_pendiente]');

SELECT * FROM [tabla_transaccional]
WHERE [campo_descripcion] = 'PRUEBA_ROLLBACK';

ROLLBACK;

SELECT COUNT(*) AS total_despues FROM [tabla_transaccional];

SELECT * FROM [tabla_transaccional]
WHERE [campo_descripcion] = 'PRUEBA_ROLLBACK';
-- Esperado: 0 filas

-- Paso 3: limpieza final de datos de prueba
DELETE FROM [tabla_transaccional]
WHERE [campo_descripcion] IN ('PRUEBA_COMMIT', 'PRUEBA_TRX_001', 'PRUEBA_TRX_002', 'PRUEBA_TRX_003');

DELETE FROM [tabla_maestra]
WHERE [campo_codigo] LIKE 'TEST_%';

DELETE FROM [tabla_usuarios]
WHERE [campo_usuario] LIKE 'test_%';

SELECT COUNT(*) AS datos_prueba_restantes
FROM [tabla_transaccional]
WHERE [campo_descripcion] LIKE 'PRUEBA_%';
