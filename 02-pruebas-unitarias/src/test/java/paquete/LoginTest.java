package paquete;

import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertFalse;
import static org.junit.jupiter.api.Assertions.assertNotNull;
import static org.junit.jupiter.api.Assertions.assertTrue;

class LoginTest {

	private final LoginService loginService = new LoginService();

	@Test
	@DisplayName("Login exitoso con credenciales validas")
	void deberiaAutenticarUsuarioValido() {
		LoginRequest request = new LoginRequest("[usuario_valido]", "[clave_valida]");

		LoginResponse response = loginService.login(request);

		assertTrue(response.isSuccess());
		assertNotNull(response.getSessionToken());
		assertEquals("[mensaje_login_exitoso]", response.getMessage());
	}

	@Test
	@DisplayName("Login rechazado con clave incorrecta")
	void deberiaRechazarClaveIncorrecta() {
		LoginRequest request = new LoginRequest("[usuario_valido]", "[clave_incorrecta]");

		LoginResponse response = loginService.login(request);

		assertFalse(response.isSuccess());
		assertEquals("[mensaje_credenciales_invalidas]", response.getMessage());
	}

	@Test
	@DisplayName("Bloqueo tras maximo de intentos")
	void deberiaBloquearUsuarioTrasIntentosFallidos() {
		int maxIntentos = 3;
		for (int i = 0; i < maxIntentos; i++) {
			loginService.login(new LoginRequest("[usuario_valido]", "[clave_incorrecta]"));
		}

		LoginResponse response = loginService.login(new LoginRequest("[usuario_valido]", "[clave_incorrecta]"));

		assertFalse(response.isSuccess());
		assertEquals("[mensaje_usuario_bloqueado]", response.getMessage());
	}

	@Test
	@DisplayName("Login con usuario inactivo")
	void deberiaRechazarUsuarioInactivo() {
		LoginResponse response = loginService.login(new LoginRequest("[usuario_inactivo]", "[clave_valida]"));

		assertFalse(response.isSuccess());
		assertEquals("[mensaje_usuario_inactivo]", response.getMessage());
	}

	@Test
	@DisplayName("Login con campos vacios")
	void deberiaValidarCamposObligatorios() {
		LoginResponse response = loginService.login(new LoginRequest("", ""));

		assertFalse(response.isSuccess());
		assertEquals("[mensaje_campos_obligatorios]", response.getMessage());
	}

	@Test
	@DisplayName("Login con usuario inexistente")
	void deberiaRechazarUsuarioInexistente() {
		LoginResponse response = loginService.login(new LoginRequest("[usuario_no_existe]", "[clave_valida]"));

		assertFalse(response.isSuccess());
		assertEquals("[mensaje_credenciales_invalidas]", response.getMessage());
	}

	@Test
	@DisplayName("Generacion de token de sesion")
	void deberiaGenerarTokenSesionCuandoLoginEsValido() {
		LoginResponse response = loginService.login(new LoginRequest("[usuario_valido]", "[clave_valida]"));

		assertNotNull(response.getSessionToken());
		assertTrue(response.getSessionToken().length() > 5);
	}

	// Clases placeholder para adaptar a tu proyecto real.
	static class LoginService {
		LoginResponse login(LoginRequest request) {
			if (request.username() == null || request.password() == null
					|| request.username().isBlank() || request.password().isBlank()) {
				return new LoginResponse(false, "[mensaje_campos_obligatorios]", null);
			}
			if ("[usuario_inactivo]".equals(request.username())) {
				return new LoginResponse(false, "[mensaje_usuario_inactivo]", null);
			}
			if ("[usuario_no_existe]".equals(request.username())) {
				return new LoginResponse(false, "[mensaje_credenciales_invalidas]", null);
			}
			if ("[clave_valida]".equals(request.password())) {
				return new LoginResponse(true, "[mensaje_login_exitoso]", "[token_sesion]");
			}
			return new LoginResponse(false, "[mensaje_credenciales_invalidas]", null);
		}
	}

	record LoginRequest(String username, String password) {}

	static class LoginResponse {
		private final boolean success;
		private final String message;
		private final String sessionToken;

		LoginResponse(boolean success, String message, String sessionToken) {
			this.success = success;
			this.message = message;
			this.sessionToken = sessionToken;
		}

		boolean isSuccess() {
			return success;
		}

		String getMessage() {
			return message;
		}

		String getSessionToken() {
			return sessionToken;
		}
	}
}
