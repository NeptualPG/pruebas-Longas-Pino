# 20 criterios de aceptacion (formato Dado / Cuando / Entonces)

## Login

1. Dado un usuario activo en [tabla_usuarios], cuando envia credenciales validas a [endpoint_login], entonces el sistema autentica y retorna sesion valida.
2. Dado un usuario con [campo_estado] inactivo, cuando intenta iniciar sesion en [endpoint_login], entonces el sistema rechaza el acceso con mensaje controlado.
3. Dado un usuario con clave incorrecta, cuando supera [max_intentos_login] intentos, entonces el sistema bloquea temporalmente la cuenta.
4. Dado un usuario bloqueado temporalmente, cuando intenta iniciar sesion antes de [tiempo_desbloqueo], entonces el sistema mantiene el bloqueo e informa tiempo restante.
5. Dado un usuario que solicita recuperar clave en [endpoint_forgot_password], cuando el correo existe, entonces el sistema genera token de recuperacion y notifica por canal definido.
6. Dado un token de recuperacion expirado, cuando se usa en [endpoint_reset_password], entonces el sistema rechaza el cambio de clave.
7. Dado un usuario con 2FA habilitado, cuando valida codigo correcto en [endpoint_2fa_verify], entonces el sistema completa autenticacion y crea sesion.

## Modulo maestro CRUD

8. Dado un usuario con rol autorizado, cuando crea un registro en [endpoint_maestro_create], entonces el sistema persiste el registro en [tabla_maestra].
9. Dado un registro existente en [tabla_maestra], cuando se consulta por id en [endpoint_maestro_get_by_id], entonces el sistema retorna datos completos y consistentes.
10. Dado filtros validos, cuando se consulta [endpoint_maestro_list], entonces el sistema retorna listado paginado con metadatos de paginacion.
11. Dado un registro existente, cuando se actualiza en [endpoint_maestro_update] con datos validos, entonces el sistema guarda cambios y conserva trazabilidad.
12. Dado un registro referenciado por [tabla_transaccional], cuando se intenta eliminar desde [endpoint_maestro_delete], entonces el sistema impide borrado fisico y responde error de negocio.
13. Dado un payload invalido en campos obligatorios, cuando se crea o actualiza en modulo maestro, entonces el sistema valida y reporta errores por campo.
14. Dado dos solicitudes concurrentes para actualizar el mismo registro maestro, cuando ocurre conflicto de version, entonces el sistema resuelve segun [estrategia_concurrencia].

## Modulo transaccional

15. Dado una solicitud valida de alta transaccional en [endpoint_transaccional_create], cuando existen datos maestros relacionados, entonces el sistema crea transaccion en [tabla_transaccional].
16. Dado una solicitud transaccional con referencia inexistente a [tabla_maestra], cuando se procesa la operacion, entonces el sistema rechaza por integridad referencial.
17. Dado una transaccion en estado [estado_inicial], cuando se ejecuta la accion [evento_cambio_estado], entonces el sistema cambia al estado [estado_destino] segun reglas de negocio.
18. Dado una operacion transaccional que afecta varias tablas, cuando falla un paso intermedio, entonces el sistema realiza rollback completo.
19. Dado una transaccion confirmada, cuando se consulta historial en [endpoint_transaccional_historial], entonces el sistema muestra trazabilidad de eventos y usuario responsable.
20. Dado un usuario sin permisos sobre modulo transaccional, cuando intenta ejecutar [endpoint_transaccional_aprobar], entonces el sistema responde acceso denegado sin modificar datos.
