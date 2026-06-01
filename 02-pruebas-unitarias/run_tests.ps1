# Script para ejecutar Pruebas Unitarias - JAANSTYLE
# Uso: .\run_tests.ps1

Write-Host "================================" -ForegroundColor Cyan
Write-Host "Pruebas Unitarias - JAANSTYLE" -ForegroundColor Cyan
Write-Host "Fase 2: Pruebas Unitarias" -ForegroundColor Cyan
Write-Host "================================" -ForegroundColor Cyan
Write-Host ""

# Verificar si pytest está instalado
Write-Host "Verificando instalación de pytest..." -ForegroundColor Yellow
$pytestCheck = python -m pytest --version 2>&1
if ($LASTEXITCODE -ne 0) {
    Write-Host "pytest no está instalado. Instalando..." -ForegroundColor Yellow
    pip install -r requirements.txt
}

Write-Host $pytestCheck -ForegroundColor Green
Write-Host ""

# Crear directorio de evidencias si no existe
if (-not (Test-Path "evidencias")) {
    New-Item -ItemType Directory -Path "evidencias" | Out-Null
    Write-Host "Creado directorio: evidencias/" -ForegroundColor Green
}

# Ejecutar tests
Write-Host "Ejecutando pruebas unitarias..." -ForegroundColor Cyan
Write-Host "================================" -ForegroundColor Cyan
Write-Host ""

# Ejecutar con reportes
python -m pytest src/test/python/test_auth.py `
    -v `
    --tb=short `
    --html=evidencias/test_report.html `
    --self-contained-html `
    -rA

$testResult = $LASTEXITCODE

Write-Host ""
Write-Host "================================" -ForegroundColor Cyan

if ($testResult -eq 0) {
    Write-Host "✓ Todas las pruebas pasaron exitosamente" -ForegroundColor Green
} else {
    Write-Host "✗ Algunas pruebas fallaron" -ForegroundColor Red
}

Write-Host "Reporte generado: evidencias/test_report.html" -ForegroundColor Yellow
Write-Host "================================" -ForegroundColor Cyan

exit $testResult
