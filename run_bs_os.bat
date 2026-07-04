@echo off
chcp 65001 >nul
title BS_OS Launcher

echo Starting BS_OS Launcher...
python "%~dp0bs_os_launcher.py"

if errorlevel 1 (
    echo.
    echo Failed to start BS_OS. Please make sure Python is installed.
    pause
)
