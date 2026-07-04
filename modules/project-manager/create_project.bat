@echo off
chcp 65001 >nul
title BS Project Manager - Create Project

echo BS Project Manager v0.4-alpha
echo.
set /p PROJECT_NAME=Project name: 
set /p CLIENT_NAME=Client name optional: 
set /p DESIGNER_NAME=Designer optional: 
set /p PROJECT_STAGE=Stage optional, default concept: 

if "%PROJECT_STAGE%"=="" set PROJECT_STAGE=concept

python "%~dp0..\..\scripts\project_manager.py" --name "%PROJECT_NAME%" --client "%CLIENT_NAME%" --designer "%DESIGNER_NAME%" --stage "%PROJECT_STAGE%"

echo.
pause
