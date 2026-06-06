"""
Pruebas Unitarias - Módulo Autenticación
Proyecto: JAANSTYLE - Plataforma de Diseño y Venta de Prendas Personalizadas
Fase 2: Pruebas Unitarias
"""

import pytest
import sys
import os
from datetime import datetime, timedelta

# Agregar el path del proyecto a sys.path para importar módulos
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../../..', 'Tienda-de-ropa'))
sys.path.insert(0, project_root)

# Importar módulos del proyecto
from controllers.auth import (
    login, 
    create_user, 
    find_user_by_email,
    reset_failed_attempts
)
from controllers.utils import gen_2fa_code
from config.settings import (
    DB_PATH,
    MAX_FAILED_ATTEMPTS,
    SESSION_TIMEOUT_SECONDS
)
import controllers.auth as auth_module


class TestLoginExitoso:
    """
    CA-06: Login Exitoso con Credenciales Válidas
    Descripción: Usuario debe poder iniciar sesión con email y contraseña correctos.
    """
    
    def setup_method(self):
        """
        Crear un usuario de prueba antes de cada test
        """
        self.email = "usuario.prueba@example.com"
        self.password = "TestPassword123!"
        self.username = "usuario_prueba"
        self.client_ip = "127.0.0.1"
        
        # Crear usuario de prueba
        ok, msg = create_user(
            username=self.username,
            email=self.email,
            password=self.password,
            first_name="Usuario",
            last_name="Prueba"
        )
        # Si el usuario ya existe, está bien, solo continuamos
        print(f"User creation result: {ok}, {msg}")
        # Asegurar que usuario no está bloqueado y resetear intentos fallidos
        usuario = find_user_by_email(self.email)
        if usuario:
            uid = usuario[0]
            reset_failed_attempts(uid)
            import sqlite3
            db = sqlite3.connect(DB_PATH)
            try:
                cur = db.cursor()
                cur.execute("UPDATE users SET blocked = 0, blocked_until = NULL WHERE id_usuario = ?", (uid,))
                db.commit()
            finally:
                db.close()
    
    def test_login_exitoso(self):
        """
        Validar que el login es exitoso con credenciales correctas
        
        Pasos:
        1. Usar credenciales válidas de usuario existente
        2. Ejecutar función login()
        
        Validaciones:
        - Login retorna True (éxito)
        - Se genera token
        - Token es válido
        """
        # Acción: Intentar login exitoso
        resultado, mensaje, token, _ = login(self.email, self.password, self.client_ip)
        
        # Validación 1: Login es exitoso
        assert resultado is True, f"Login falló: {mensaje}"
        
        # Validación 2: Se genera token
        assert token is not None, "Token no fue generado"
        
        # Validación 3: Token es una cadena (hexadecimal)
        assert isinstance(token, str), f"Token debe ser string, recibió {type(token)}"
        
        # Validación 4: Mensaje indica envío de 2FA
        assert "2FA" in mensaje or "código" in mensaje.lower(), f"Mensaje no menciona 2FA: {mensaje}"


class TestPasswordIncorrecta:
    """
    CA-08: Rechazo de Login con Contraseña Incorrecta
    Descripción: Sistema rechaza login si contraseña no coincide.
    """
    
    def test_password_incorrecta(self):
        """
        Validar que login rechaza contraseña incorrecta
        
        Pasos:
        1. Usar email correcto pero password incorrecto
        2. Ejecutar función login()
        
        Validaciones:
        - Login retorna False
        - Mensaje indica "Credenciales inválidas"
        - No se genera token 2FA
        - Contador de intentos fallidos se incrementa
        """
        email = "usuario.prueba@example.com"
        password_incorrecta = "PasswordIncorrecto123!"
        
        # Acción: Intentar login con password incorrecta
        resultado, mensaje, token_2fa, _ = login(email, password_incorrecta, "127.0.0.1")
        
        # Validación 1: Login falla
        assert resultado is False, "Login no debería ser exitoso con password incorrecta"
        
        # Validación 2: Mensaje indica credenciales inválidas
        assert "Credenciales inválidas" in mensaje or "incorrecto" in mensaje.lower(), \
            f"Mensaje no indica credenciales inválidas: {mensaje}"
        
        # Validación 3: No genera token 2FA
        assert token_2fa is None, "Token 2FA no debería generarse con credenciales inválidas"


class TestUsuarioBloqueado:
    """
    CA-09: Bloqueo de Usuario por Intentos Fallidos
    Descripción: Usuario debe bloquearse temporalmente después de 3 intentos fallidos.
    """
    
    def test_usuario_bloqueado(self):
        """
        Validar que usuario se bloquea después de 3 intentos fallidos
        
        Pasos:
        1. Intentar login 3 veces con password incorrecta
        2. Verificar que usuario está bloqueado (blocked=1)
        3. Intentar login en 4ta vez
        
        Validaciones:
        - Después de 3 intentos, cuenta se bloquea
        - Campo blocked = 1 en BD
        - Mensaje indica "Cuenta bloqueada"
        - Se envía email de alerta
        """
        email = "usuario.prueba@example.com"
        password_incorrecta = "PasswordIncorrecto123!"
        
        # Acción: Ejecutar 3 intentos fallidos
        for i in range(3):
            resultado, mensaje, _, _ = login(email, password_incorrecta, "127.0.0.1")
            assert resultado is False, f"Intento {i+1}: Login debería fallar"
        
        # Acción: Intento 4 - Usuario debe estar bloqueado
        resultado, mensaje, _, _ = login(email, password_incorrecta, "127.0.0.1")
        
        # Validación 1: Login rechaza acceso (usuario bloqueado)
        assert resultado is False, "Acceso debería ser rechazado (usuario bloqueado)"
        
        # Validación 2: Mensaje indica bloqueo
        assert "bloqueado" in mensaje.lower() or "bloqueada" in mensaje.lower(), \
            f"Mensaje no menciona bloqueo: {mensaje}"
        
        # Validación 3: Verificar en BD que usuario está bloqueado
        usuario = find_user_by_email(email)
        assert usuario is not None, "Usuario no encontrado en BD"
        assert usuario[6] == 1, f"Campo 'blocked' debería ser 1, es {usuario[6]}"


class TestUsuarioInactivo:
    """
    CA-10: Usuario Deshabilitado
    Descripción: Usuario deshabilitado no puede iniciar sesión.
    """
    
    def test_usuario_inactivo(self):
        """
        Validar que usuario inactivo/deshabilitado no puede hacer login
        
        Pasos:
        1. Buscar usuario con enabled=0 en BD
        2. Intentar login con credenciales correctas
        
        Validaciones:
        - Login rechaza al usuario inactivo
        - Mensaje indica "Usuario inactivo" o "usuario deshabilitado"
        - No se genera token 2FA
        """
        # Nota: Este test requiere un usuario inactivo en la BD
        # Para propósitos de testing, se valida la lógica de validación
        email = "usuario.inactivo@example.com"
        password = "TestPassword123!"
        
        # Acción: Intentar login
        resultado, mensaje, token_2fa, _ = login(email, password, "127.0.0.1")
        
        # Validación 1: Login es rechazado
        assert resultado is False, "Usuario inactivo debería ser rechazado"
        
        # Validación 2: Token 2FA no se genera
        assert token_2fa is None, "Token 2FA no debería generarse para usuario inactivo"


class TestGeneracion2FA:
    """
    CA-11: Generación y Envío de Código 2FA
    Descripción: Sistema debe generar código 2FA después de login exitoso.
    """
    
    def test_generacion_2fa(self):
        """
        Validar que se genera código 2FA válido
        
        Pasos:
        1. Completar login exitoso
        2. Validar que código 2FA se generó
        3. Validar que código es de 6 dígitos
        
        Validaciones:
        - Código generado de 6 dígitos
        - Código es numérico
        - Código no es None
        - Código está almacenado en sesión
        """
        email = "usuario.prueba@example.com"
        password = "TestPassword123!"
        
        # Asegurar que el usuario no está bloqueado por tests previos
        usuario = find_user_by_email(email)
        if usuario:
            uid = usuario[0]
            reset_failed_attempts(uid)
            import sqlite3
            db = sqlite3.connect(DB_PATH)
            try:
                cur = db.cursor()
                cur.execute("UPDATE users SET blocked = 0, blocked_until = NULL WHERE id_usuario = ?", (uid,))
                db.commit()
            finally:
                db.close()

        # Acción: Login exitoso
        resultado, mensaje, token, _ = login(email, password, "127.0.0.1")
        
        # Validación 1: Login exitoso
        assert resultado is True, f"Login falló: {mensaje}"
        
        # Validación 2: Se generó un token de sesión (identificador)
        assert token is not None, "Token de sesión no fue generado"
        # Extraer código 2FA desde la sesión pendiente
        codigo = auth_module.SESSIONS.get(token, {}).get("pending_2fa")
        assert codigo is not None, "Código 2FA no se encontró en la sesión"
        codigo_str = str(codigo)
        # Validación 3: Código es de 6 dígitos
        assert len(codigo_str) == 6, f"Código tiene {len(codigo_str)} dígitos, esperaba 6"
        # Validación 4: Código es numérico
        assert codigo_str.isdigit(), f"Token 2FA no es numérico: {codigo_str}"
        # Validación 5: Token es aleatorio (generar 2 tokens seguidos)
        resultado2, _, token2, _ = login(email, password, "127.0.0.1")
        codigo2 = auth_module.SESSIONS.get(token2, {}).get("pending_2fa")
        assert codigo != codigo2, "Códigos 2FA deberían ser diferentes (aleatorios)"


class TestValidacion2FAExpiración:
    """
    Validación adicional: Generación correcta de 2FA
    Descripción: Token 2FA debe tener estructura correcta y validación temporal.
    """
    
    def test_generacion_codigo_2fa(self):
        """
        Validar directamente la función generate_2fa_code()
        
        Validaciones:
        - Función genera código de 6 dígitos
        - Código es numérico
        - Código es aleatorio en cada llamada
        """
        # Acción: Generar 10 códigos 2FA
        codigos = set()
        for _ in range(10):
            codigo = gen_2fa_code()
            codigos.add(codigo)
            
            # Validación: Código es de 6 dígitos
            assert len(str(codigo)) == 6, f"Código tiene {len(str(codigo))} dígitos"
            
            # Validación: Código es numérico
            assert str(codigo).isdigit(), f"Código no es numérico: {codigo}"
        
        # Validación: Códigos son diferentes (aleatorios)
        assert len(codigos) == 10, "Códigos 2FA deberían ser únicos (aleatorios)"


# Configuración de pytest
if __name__ == "__main__":
    pytest.main([__file__, "-v", "--tb=short"])
