# Guia rapida OWASP ZAP

## Objetivo

Ejecutar escaneo de seguridad basico del sistema real y registrar hallazgos.

## Pasos

1. Abrir ZAP y elegir sesion temporal.
2. En URL to attack, ingresar [url_sistema].
3. Ejecutar Attack.
4. Esperar fin del escaneo.
5. Revisar pestana Alerts.
6. Exportar HTML en 06-seguridad/reporte-zap.html.

## Evidencias minimas

- Captura de escaneo en progreso o terminado.
- Captura de alertas encontradas.
- Reporte HTML exportado.
- Tabla de vulnerabilidades y propuesta en reporte final.

## Escala de alertas

- High: vulnerabilidad critica
- Medium: vulnerabilidad moderada
- Low: riesgo bajo
- Informational: hallazgo informativo
