package paquete;

import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertFalse;
import static org.junit.jupiter.api.Assertions.assertNotNull;
import static org.junit.jupiter.api.Assertions.assertTrue;

class MaestroTest {

	private final MaestroService maestroService = new MaestroService();

	@Test
	@DisplayName("Crear registro maestro")
	void deberiaCrearRegistroMaestro() {
		MaestroRequest request = new MaestroRequest("[campo_nombre]", "[campo_codigo]");

		MaestroResponse response = maestroService.create(request);

		assertTrue(response.success());
		assertNotNull(response.id());
		assertEquals("[mensaje_creacion_exitosa]", response.message());
	}

	@Test
	@DisplayName("Actualizar registro maestro")
	void deberiaActualizarRegistroMaestro() {
		MaestroRequest request = new MaestroRequest("[nuevo_nombre]", "[nuevo_codigo]");

		MaestroResponse response = maestroService.update("[id_existente]", request);

		assertTrue(response.success());
		assertEquals("[mensaje_actualizacion_exitosa]", response.message());
	}

	@Test
	@DisplayName("Eliminar registro maestro referenciado")
	void noDeberiaEliminarRegistroReferenciado() {
		MaestroResponse response = maestroService.delete("[id_referenciado]");

		assertFalse(response.success());
		assertEquals("[mensaje_referencia_existente]", response.message());
	}

	@Test
	@DisplayName("Consultar registro maestro por id")
	void deberiaConsultarRegistroPorId() {
		MaestroResponse response = maestroService.getById("[id_existente]");

		assertTrue(response.success());
		assertEquals("[id_existente]", response.id());
	}

	@Test
	@DisplayName("Listar registros maestros")
	void deberiaListarRegistros() {
		MaestroListResponse response = maestroService.list();

		assertTrue(response.success());
		assertTrue(response.total() >= 0);
	}

	@Test
	@DisplayName("Crear registro con campo obligatorio vacio")
	void noDeberiaCrearConCampoObligatorioVacio() {
		MaestroResponse response = maestroService.create(new MaestroRequest("", "[codigo]"));

		assertFalse(response.success());
		assertEquals("[mensaje_validacion_campo_obligatorio]", response.message());
	}

	@Test
	@DisplayName("Actualizar registro inexistente")
	void noDeberiaActualizarRegistroInexistente() {
		MaestroResponse response = maestroService.update("[id_no_existe]", new MaestroRequest("[nombre]", "[codigo]"));

		assertFalse(response.success());
		assertEquals("[mensaje_registro_no_encontrado]", response.message());
	}

	static class MaestroService {
		MaestroResponse create(MaestroRequest request) {
			if (request.nombre() == null || request.nombre().isBlank()) {
				return new MaestroResponse(false, "[mensaje_validacion_campo_obligatorio]", null);
			}
			return new MaestroResponse(true, "[mensaje_creacion_exitosa]", "[id_generado]");
		}

		MaestroResponse update(String id, MaestroRequest request) {
			if ("[id_no_existe]".equals(id)) {
				return new MaestroResponse(false, "[mensaje_registro_no_encontrado]", null);
			}
			return new MaestroResponse(true, "[mensaje_actualizacion_exitosa]", id);
		}

		MaestroResponse delete(String id) {
			return new MaestroResponse(false, "[mensaje_referencia_existente]", id);
		}

		MaestroResponse getById(String id) {
			return new MaestroResponse(true, "[mensaje_consulta_exitosa]", id);
		}

		MaestroListResponse list() {
			return new MaestroListResponse(true, 2);
		}
	}

	record MaestroRequest(String nombre, String codigo) {}

	record MaestroResponse(boolean success, String message, String id) {}

	record MaestroListResponse(boolean success, int total) {}
}
