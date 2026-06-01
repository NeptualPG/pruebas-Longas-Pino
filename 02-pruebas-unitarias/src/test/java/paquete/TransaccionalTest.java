package paquete;

import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertFalse;
import static org.junit.jupiter.api.Assertions.assertTrue;

class TransaccionalTest {

	private final TransaccionalService transaccionalService = new TransaccionalService();

	@Test
	@DisplayName("Crear transaccion valida")
	void deberiaCrearTransaccionValida() {
		TransaccionRequest request = new TransaccionRequest("[id_cliente]", "[id_item]", "[monto]");

		TransaccionResponse response = transaccionalService.crear(request);

		assertTrue(response.success());
		assertEquals("[estado_inicial]", response.estado());
	}

	@Test
	@DisplayName("Rechazar transaccion con referencia invalida")
	void deberiaRechazarReferenciaInvalida() {
		TransaccionRequest request = new TransaccionRequest("[id_cliente]", "[id_item_inexistente]", "[monto]");

		TransaccionResponse response = transaccionalService.crear(request);

		assertFalse(response.success());
		assertEquals("[mensaje_referencia_invalida]", response.mensaje());
	}

	@Test
	@DisplayName("Rollback ante error intermedio")
	void deberiaHacerRollbackAnteFalloIntermedio() {
		TransaccionResponse response = transaccionalService.procesarConFalloControlado("[id_transaccion]", true);

		assertFalse(response.success());
		assertEquals("[mensaje_rollback_aplicado]", response.mensaje());
	}

	@Test
	@DisplayName("Rechazar monto negativo")
	void deberiaRechazarMontoNegativo() {
		TransaccionRequest request = new TransaccionRequest("[id_cliente]", "[id_item]", "-10");

		TransaccionResponse response = transaccionalService.crear(request);

		assertFalse(response.success());
		assertEquals("[mensaje_monto_invalido]", response.mensaje());
	}

	@Test
	@DisplayName("Rechazar monto en cero")
	void deberiaRechazarMontoCero() {
		TransaccionRequest request = new TransaccionRequest("[id_cliente]", "[id_item]", "0");

		TransaccionResponse response = transaccionalService.crear(request);

		assertFalse(response.success());
		assertEquals("[mensaje_monto_invalido]", response.mensaje());
	}

	@Test
	@DisplayName("Cambio de estado permitido")
	void deberiaCambiarEstadoSegunRegla() {
		TransaccionResponse response = transaccionalService.cambiarEstado("[id_transaccion]", "[estado_en_proceso]");

		assertTrue(response.success());
		assertEquals("[estado_en_proceso]", response.estado());
	}

	@Test
	@DisplayName("Cambio de estado no permitido")
	void noDeberiaCambiarEstadoInvalido() {
		TransaccionResponse response = transaccionalService.cambiarEstado("[id_transaccion]", "[estado_invalido]");

		assertFalse(response.success());
		assertEquals("[mensaje_estado_invalido]", response.mensaje());
	}

	static class TransaccionalService {
		TransaccionResponse crear(TransaccionRequest request) {
			double monto = Double.parseDouble(request.monto());
			if (monto <= 0) {
				return new TransaccionResponse(false, "[mensaje_monto_invalido]", "[estado_error]");
			}
			if ("[id_item_inexistente]".equals(request.idItem())) {
				return new TransaccionResponse(false, "[mensaje_referencia_invalida]", "[estado_error]");
			}
			return new TransaccionResponse(true, "[mensaje_transaccion_creada]", "[estado_inicial]");
		}

		TransaccionResponse procesarConFalloControlado(String idTransaccion, boolean provocarFallo) {
			if (provocarFallo) {
				return new TransaccionResponse(false, "[mensaje_rollback_aplicado]", "[estado_revertido]");
			}
			return new TransaccionResponse(true, "[mensaje_proceso_ok]", "[estado_final]");
		}

		TransaccionResponse cambiarEstado(String idTransaccion, String nuevoEstado) {
			if ("[estado_invalido]".equals(nuevoEstado)) {
				return new TransaccionResponse(false, "[mensaje_estado_invalido]", "[estado_actual]" );
			}
			return new TransaccionResponse(true, "[mensaje_estado_actualizado]", nuevoEstado);
		}
	}

	record TransaccionRequest(String idCliente, String idItem, String monto) {}

	record TransaccionResponse(boolean success, String mensaje, String estado) {}
}
