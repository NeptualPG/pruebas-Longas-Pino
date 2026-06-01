# Fase 2: Pruebas Unitarias - JAANSTYLE

## Descripción

Pruebas unitarias del módulo de autenticación para validar:
- Credenciales correctas
- Contraseña incorrecta
- Usuario bloqueado
- Usuario inactivo/deshabilitado
- Generación de código 2FA

## Estructura

```
02-pruebas-unitarias/
├── src/test/python/
│   ├── test_auth.py          # Tests del módulo autenticación
│   └── conftest.py           # Configuración de pytest
├── evidencias/               # Reportes de ejecución
├── README.md                 # Esta documentación
└── requirements.txt          # Dependencias
```

## Pruebas Incluidas

### 1. TestLoginExitoso
**CA-06:** Validar login exitoso con credenciales correctas
- Verifica que el login retorna True
- Valida generación de código 2FA
- Comprueba que token es de 6 dígitos

### 2. TestPasswordIncorrecta  
**CA-08:** Validar rechazo con password incorrecta
- Verifica que login retorna False
- Valida mensaje "Credenciales inválidas"
- Confirma que NO se genera 2FA

### 3. TestUsuarioBloqueado
**CA-09:** Validar bloqueo después de 3 intentos fallidos
- Ejecuta 3 intentos fallidos
- Verifica que usuario está bloqueado (blocked=1)
- Confirma mensaje de bloqueo

### 4. TestUsuarioInactivo
**CA-10:** Validar rechazo de usuario deshabilitado
- Intenta login con usuario inactivo
- Verifica rechazo de acceso
- Confirma que NO se genera 2FA

### 5. TestGeneracion2FA
**CA-11:** Validar generación de código 2FA
- Comprueba código de 6 dígitos
- Valida que es numérico
- Verifica aleatoriedad en múltiples llamadas

## Instalación de Dependencias

```bash
# Activar environment Python 3.12
conda activate python312

# Instalar pytest
pip install pytest

# Opcional: instalar pytest-cov para cobertura
pip install pytest-cov
```

## Ejecución de Pruebas

### Ejecutar todos los tests
```bash
cd pruebas-Longas-Pino/02-pruebas-unitarias
pytest src/test/python/test_auth.py -v
```

### Ejecutar test específico
```bash
pytest src/test/python/test_auth.py::TestLoginExitoso::test_login_exitoso -v
```

### Ver cobertura de código
```bash
pytest src/test/python/test_auth.py --cov=../../Tienda-de-ropa/controllers/auth --cov-report=html
```

## Requisitos Previos

1. **Base de datos inicializada**
   - Usar `Tienda-de-ropa/db/database.sqlite`
   - Ejecutar `db/init_db.py` si es necesario

2. **Usuario de prueba creado**
   - Email: `usuario.prueba@example.com`
   - Password: `TestPassword123!`
   - Estado: enabled=1

3. **Ambiente Python**
   - Python 3.12+
   - pytest instalado
   - Proyecto Tienda-de-ropa accesible

## Mapeo a Criterios de Aceptación

| Test | CA | Descripción |
|------|----|----|
| test_login_exitoso | CA-06 | Login con credenciales correctas |
| test_password_incorrecta | CA-08 | Rechazo con password incorrecta |
| test_usuario_bloqueado | CA-09 | Bloqueo después de 3 intentos |
| test_usuario_inactivo | CA-10 | Rechazo de usuario inactivo |
| test_generacion_2fa | CA-11 | Generación de código 2FA |
| test_generacion_codigo_2fa | CA-11 | Validación adicional de 2FA |

## Reportes

Los reportes de ejecución se guardan en:
- `evidencias/test_report.txt` - Resumen de tests
- `evidencias/coverage_report.html` - Cobertura de código

## Próximos Pasos

Después de validar estos tests:

1. **Fase 3**: Pruebas Funcionales con Selenium
   - Automatizar flujos en navegador
   - Validar UI e interacción

2. **Fase 4**: Pruebas API con Postman
   - Validar endpoints
   - Comprobar respuestas JSON

3. **Fase 5**: Pruebas de BD
   - Integridad referencial
   - Transacciones

4. **Fase 6**: Pruebas de Seguridad
   - OWASP ZAP
   - Inyección SQL
   - XSS

---

**Versión:** 1.0  
**Fecha:** Mayo 2026  
**Autor:** QA Team
