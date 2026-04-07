@echo off
where poetry >nul 2>&1
if %errorlevel% neq 0 (
    echo Poetry is not installed or not in PATH. Please install it from https://python-poetry.org/
    pause
    exit /b 1
)

poetry install --quiet
if %errorlevel% neq 0 (
    echo Dependency installation failed.
    pause
    exit /b 1
)

poetry run qrCodeGenGUI
