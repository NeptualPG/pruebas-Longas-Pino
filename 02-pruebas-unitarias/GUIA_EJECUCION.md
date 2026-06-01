# GUÍA DE EJECUCIÓN - Fase 2: Pruebas Unitarias

## 📋 Resumen

Esta fase ejecuta **5 pruebas unitarias** del módulo de autenticación (Login) del sistema JAANSTYLE, mapeadas directamente a los criterios de aceptación CA-06, CA-08, CA-09, CA-10 y CA-11.

---

## 🚀 Inicio Rápido

### Opción 1: Usar Script PowerShell (Recomendado)

```powershell
# En PowerShell, dentro de la carpeta 02-pruebas-unitarias/
.\run_tests.ps1
```

El script automáticamente:
- ✅ Verifica pytest instalado
- ✅ Instala dependencias si falta
- ✅ Crea carpeta `evidencias/`
- ✅ Ejecuta todos los tests
- ✅ Genera reporte HTML

### Opción 2: Comando Manual

```bash
# Activar Python 3.12
conda activate python312

# Navegar a carpeta de pruebas
cd pruebas-Longas-Pino/02-pruebas-unitarias

# Instalar dependencias
pip install -r requirements.txt

# Ejecutar tests
pytest src/test/python/test_auth.py -v
```

---

## 📊 Pruebas Incluidas

### 1️⃣ TestLoginExitoso (CA-06)
```
✓ Usuario loguea con credenciales correctas
✓ Se genera código 2FA de 6 dígitos
✓ Mensaje confirma envío de 2FA
```

### 2️⃣ TestPasswordIncorrecta (CA-08)
```
✓ Login rechaza contraseña incorrecta
✓ Mensaje indica "Credenciales inválidas"
✓ NO se genera token 2FA
```

### 3️⃣ TestUsuarioBloqueado (CA-09)
```
✓ Después de 3 intentos fallidos, cuenta se bloquea
✓ Campo 'blocked' = 1 en BD
✓ Mensaje indica "Cuenta bloqueada"
```

### 4️⃣ TestUsuarioInactivo (CA-10)
```
✓ Usuario deshabilitado es rechazado
✓ NO se genera token 2FA
✓ Acceso es denegado
```

### 5️⃣ TestGeneracion2FA (CA-11)
```
✓ Código 2FA es de 6 dígitos
✓ Código es numérico
✓ Códigos son únicos (aleatorios)
```

---

## 📝 Requisitos Previos

### 1. Python 3.12 Instalado
```bash
conda activate python312
python --version  # Debe ser 3.12.x
```

### 2. Usuario de Prueba en BD
La BD debe tener este usuario:
- **Email:** `usuario.prueba@example.com`
- **Password:** `TestPassword123!`
- **Estado:** `enabled = 1`

Para crear el usuario manualmente:

```python
# Ejecutar dentro de Tienda-de-ropa/
from controllers.auth import create_user

success, msg = create_user(
    email="usuario.prueba@example.com",
    username="usuario_prueba",
    password="TestPassword123!",
    first_name="Usuario",
    last_name="Prueba",
    id_tipo_documento="CC",
    documento="1234567890",
    address1="Calle Test 123",
    phone1="3001234567"
)
print(f"Usuario creado: {success} - {msg}")
```

### 3. Base de Datos Inicializada
```bash
# Si la BD no existe, crear:
cd Tienda-de-ropa
python db/init_db.py
```

---

## ⚙️ Ejecución Detallada

### Ver Toda la Salida

```bash
pytest src/test/python/test_auth.py -v --tb=long
```

### Ejecutar Test Específico

```bash
# Solo TestLoginExitoso
pytest src/test/python/test_auth.py::TestLoginExitoso -v

# Solo test_password_incorrecta
pytest src/test/python/test_auth.py::TestPasswordIncorrecta::test_password_incorrecta -v
```

### Ejecutar Pruebas con Cobertura

```bash
pytest src/test/python/test_auth.py \
  --cov=../../../../Tienda-de-ropa/controllers/auth \
  --cov-report=html \
  --cov-report=term
```

Esto genera `htmlcov/index.html` con cobertura detallada.

### Modo Silencioso (Solo Resumen)

```bash
pytest src/test/python/test_auth.py -q
```

---

## 📈 Salida Esperada

### ✅ Todas las Pruebas Pasan

```
test_auth.py::TestLoginExitoso::test_login_exitoso PASSED                [20%]
test_auth.py::TestPasswordIncorrecta::test_password_incorrecta PASSED     [40%]
test_auth.py::TestUsuarioBloqueado::test_usuario_bloqueado PASSED        [60%]
test_auth.py::TestUsuarioInactivo::test_usuario_inactivo PASSED          [80%]
test_auth.py::TestGeneracion2FA::test_generacion_2fa PASSED              [100%]

================== 5 passed in 0.52s ==================
```

### ❌ Si Alguna Falla

Pytest mostrará:
```
FAILED test_auth.py::TestLoginExitoso::test_login_exitoso - AssertionError: ...

================== 1 failed, 4 passed in 0.78s ==================
```

---

## 🔍 Verificación Manual de Requisitos

Antes de ejecutar tests, verificar:

### 1. BD Accesible
```bash
# Desde Tienda-de-ropa/
python -c "
import sqlite3
conn = sqlite3.connect('db/database.sqlite')
cursor = conn.cursor()
cursor.execute('SELECT COUNT(*) FROM users')
print(f'Total usuarios en BD: {cursor.fetchone()[0]}')
conn.close()
"
```

### 2. Usuario de Prueba Existe
```bash
# Desde Tienda-de-ropa/
python -c "
import sqlite3
conn = sqlite3.connect('db/database.sqlite')
cursor = conn.cursor()
cursor.execute(\"SELECT id, correo, enabled FROM users WHERE correo='usuario.prueba@example.com'\")
row = cursor.fetchone()
if row:
    print(f'Usuario encontrado: ID={row[0]}, Email={row[1]}, Enabled={row[2]}')
else:
    print('Usuario de prueba NO ENCONTRADO')
conn.close()
"
```

### 3. Módulo auth.py Accesible
```bash
# Desde pruebas-Longas-Pino/02-pruebas-unitarias/
python -c "
import sys
sys.path.insert(0, '../../../Tienda-de-ropa')
from controllers.auth import login, generate_2fa_code
print('✓ auth.py importado exitosamente')
print(f'✓ Funciones disponibles: login, generate_2fa_code')
"
```

---

## 📁 Estructura Generada

```
02-pruebas-unitarias/
├── src/test/python/
│   ├── __init__.py
│   ├── conftest.py                 # Configuración pytest
│   └── test_auth.py                # 5 tests de autenticación
├── evidencias/
│   ├── test_report.html            # Reporte después de ejecutar
│   └── coverage_report.html        # Cobertura (opcional)
├── pytest.ini                      # Config pytest
├── requirements.txt                # Dependencias
├── run_tests.ps1                   # Script PowerShell
└── README.md                       # Documentación
```

---

## 🐛 Solución de Problemas

### Problema: "ModuleNotFoundError: No module named 'controllers'"

**Solución:** Verificar que la ruta al proyecto Tienda-de-ropa es correcta en `test_auth.py` línea 14:

```python
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../../..', 'Tienda-de-ropa'))
```

Debe apuntar a: `C:\Users\juand\Order\projects\StayConnect\Jeanstyle\Tienda-de-ropa`

### Problema: "No such table: users"

**Solución:** La BD no está inicializada. Ejecutar:

```bash
cd Tienda-de-ropa
python db/init_db.py
```

### Problema: "Usuario de prueba no encontrado"

**Solución:** Crear el usuario manualmente:

```bash
cd Tienda-de-ropa
python -c "
from controllers.auth import create_user
success, msg = create_user(
    email='usuario.prueba@example.com',
    username='usuario_prueba',
    password='TestPassword123!',
    first_name='Usuario',
    last_name='Prueba',
    id_tipo_documento='CC',
    documento='1234567890',
    address1='Calle Test 123',
    phone1='3001234567'
)
print(f'Resultado: {success} - {msg}')
"
```

### Problema: "pytest: command not found"

**Solución:** Instalar pytest:

```bash
pip install pytest pytest-cov pytest-html
```

---

## ✅ Checklist Pre-Ejecución

Antes de ejecutar los tests:

- [ ] Python 3.12 activado (`conda activate python312`)
- [ ] Pytest instalado (`pip install -r requirements.txt`)
- [ ] BD `database.sqlite` existe
- [ ] Usuario `usuario.prueba@example.com` existe en BD
- [ ] Usuario tiene `enabled=1`
- [ ] Contraseña es `TestPassword123!`
- [ ] Módulo `controllers/auth.py` es accesible
- [ ] Proyecto `Tienda-de-ropa` está en ruta correcta

---

## 📊 Próximos Pasos Después de Fase 2

1. **Fase 3**: Pruebas Funcionales con Selenium (automatizar navegador)
2. **Fase 4**: Pruebas API con Postman (validar endpoints)
3. **Fase 5**: Pruebas de BD (integridad referencial)
4. **Fase 6**: Pruebas de Seguridad (OWASP ZAP, inyección SQL, XSS)

---

**Versión:** 1.0  
**Fecha:** Mayo 2026  
**Autor:** QA Team
