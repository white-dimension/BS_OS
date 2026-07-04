@echo off
chcp 65001 >nul
title BS Recent Projects

python "%~dp0..\..\recent_projects_ui.py"

if errorlevel 1 (
    echo.
    echo Failed to start BS Recent Projects.
    pause
)
