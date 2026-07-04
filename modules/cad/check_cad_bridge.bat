@echo off
chcp 65001 >nul
title BS_OS CAD Bridge Check

echo Checking BS_OS CAD Bridge...
echo.
python "%~dp0..\..\scripts\cad_bridge.py"
echo.
pause
