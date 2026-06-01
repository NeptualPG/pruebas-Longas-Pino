"""
Configuración de pytest para Pruebas Unitarias - JAANSTYLE
"""

import pytest
import sys
import os

# Agregar path del proyecto Tienda-de-ropa
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..', 'Tienda-de-ropa'))
if project_root not in sys.path:
    sys.path.insert(0, project_root)


@pytest.fixture(scope="session")
def setup_test_environment():
    """
    Configuración inicial para los tests
    """
    print("\n" + "="*60)
    print("Iniciando Pruebas Unitarias - JAANSTYLE")
    print("="*60)
    
    yield
    
    print("\n" + "="*60)
    print("Pruebas Unitarias Completadas")
    print("="*60)


@pytest.fixture
def test_user_email():
    """
    Email del usuario de prueba
    """
    return "usuario.prueba@example.com"


@pytest.fixture
def test_user_password():
    """
    Contraseña del usuario de prueba
    """
    return "TestPassword123!"


@pytest.fixture
def test_user_data():
    """
    Datos de usuario de prueba
    """
    return {
        "email": "usuario.prueba@example.com",
        "password": "TestPassword123!",
        "username": "usuario_prueba",
        "first_name": "Usuario",
        "last_name": "Prueba"
    }


# Configuración de pytest.ini puede ir aquí también
def pytest_configure(config):
    """
    Hook para configuración inicial de pytest
    """
    config.addinivalue_line(
        "markers", "unit: Pruebas unitarias"
    )
    config.addinivalue_line(
        "markers", "auth: Pruebas del módulo autenticación"
    )
    config.addinivalue_line(
        "markers", "slow: Pruebas lentas (>1s)"
    )


def pytest_collection_modifyitems(config, items):
    """
    Modificar items de prueba antes de ejecutar
    """
    for item in items:
        # Marcar pruebas de auth
        if "test_auth" in item.nodeid:
            item.add_marker(pytest.mark.auth)
            item.add_marker(pytest.mark.unit)
