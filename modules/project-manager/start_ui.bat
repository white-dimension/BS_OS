@echo off
chcp 65001 >nul
title BS Project Manager UI

python "%~dp0..\..\project_manager_ui.py"

if errorlevel 1 (
    echo.
    echo Failed to start BS Project Manager UI.
    pause
)
