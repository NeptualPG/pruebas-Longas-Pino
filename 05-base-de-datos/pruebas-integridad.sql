-- Script 2: pruebas-integridad.sql
-- Proposito: detectar inconsistencias de datos post-ejecucion.

-- Paso 1: integridad referencial
SELECT t.*
FROM [tabla_transaccional] t
LEFT JOIN [tabla_usuarios] u ON t.[campo_id_usuario] = u.[campo_id]
WHERE u.[campo_id] IS NULL;
-- Esperado: 0 filas

SELECT t.*
FROM [tabla_transaccional] t
LEFT JOIN [tabla_maestra] m ON t.[campo_id_maestro] = m.[campo_id]
WHERE m.[campo_id] IS NULL;
-- Esperado: 0 filas

-- Paso 2: unicidad
SELECT [campo_codigo], COUNT(*) AS cantidad
FROM [tabla_maestra]
GROUP BY [campo_codigo]
HAVING COUNT(*) > 1;
-- Esperado: 0 filas

SELECT [campo_usuario], COUNT(*) AS cantidad
FROM [tabla_usuarios]
GROUP BY [campo_usuario]
HAVING COUNT(*) > 1;
-- Esperado: 0 filas

-- Paso 3: campos obligatorios
SELECT * FROM [tabla_usuarios]
WHERE [campo_nombre] IS NULL OR [campo_nombre] = '';
-- Esperado: 0 filas

SELECT * FROM [tabla_transaccional]
WHERE [campo_fecha] IS NULL;
-- Esperado: 0 filas

SELECT * FROM [tabla_maestra]
WHERE [campo_codigo] IS NULL OR [campo_codigo] = '';
-- Esperado: 0 filas

-- Paso 4: rangos y dominios
SELECT * FROM [tabla_transaccional]
WHERE [campo_monto] <= 0;
-- Esperado: 0 filas

SELECT * FROM [tabla_transaccional]
WHERE [campo_estado] NOT IN ('[estado_completada]', '[estado_pendiente]', '[estado_cancelada]');
-- Esperado: 0 filas

-- Paso 5: resumen final de integridad
SELECT 'Usuarios totales' AS concepto, COUNT(*) AS cantidad
FROM [tabla_usuarios]
UNION ALL
SELECT 'Usuarios activos', COUNT(*)
FROM [tabla_usuarios] WHERE [campo_activo] = 1
UNION ALL
SELECT 'Registros maestros', COUNT(*)
FROM [tabla_maestra]
UNION ALL
SELECT 'Transacciones totales', COUNT(*)
FROM [tabla_transaccional]
UNION ALL
SELECT 'Transacciones completadas', COUNT(*)
FROM [tabla_transaccional] WHERE [campo_estado] = '[estado_completada]';
