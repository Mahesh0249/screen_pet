@echo off
:: ============================================================
::  Gremsworth Desktop Pet - One-Click Setup
::  Run ONCE. He'll be there every time you boot.
:: ============================================================

setlocal EnableDelayedExpansion
title Gremsworth Setup

echo.
echo  ╔══════════════════════════════════════════╗
echo  ║   GREMSWORTH — Desktop Goblin Setup      ║
echo  ║   He's friendly. Mostly. Don't push it.  ║
echo  ╚══════════════════════════════════════════╝
echo.

:: ── 1. Check Python ──────────────────────────────────────────
python --version >nul 2>&1
if errorlevel 1 (
    echo  [ERROR] Python not found.
    echo  Install from https://python.org — tick "Add to PATH"
    pause
    exit /b 1
)
echo  [OK] Python found.

:: ── 2. Install dependencies ──────────────────────────────────
echo  [..] Installing psutil...
python -m pip install psutil --quiet
if errorlevel 1 (
    echo  [ERROR] Failed. Check internet connection.
    pause
    exit /b 1
)
echo  [OK] Dependencies ready.

:: ── 3. Locate script ─────────────────────────────────────────
set "SCRIPT_DIR=%~dp0"
set "SCRIPT=%SCRIPT_DIR%gremsworth.py"

if not exist "%SCRIPT%" (
    echo  [ERROR] Cannot find gremsworth.py next to this file.
    pause
    exit /b 1
)
echo  [OK] Found gremsworth.py

:: ── 4. Silent launcher (no console window) ───────────────────
set "VBS=%SCRIPT_DIR%run_gremsworth.vbs"
(
    echo Set WShell = CreateObject("WScript.Shell"^)
    echo WShell.Run "pythonw ""%SCRIPT%""", 0, False
) > "%VBS%"
echo  [OK] Silent launcher created.

:: ── 5. Add to Startup ────────────────────────────────────────
set "STARTUP=%APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup"
set "SHORTCUT=%STARTUP%\Gremsworth.vbs"
copy /Y "%VBS%" "%SHORTCUT%" >nul
echo  [OK] Gremsworth will appear on every startup.

:: ── 6. Summon him right now ───────────────────────────────────
echo  [..] Summoning Gremsworth...
cscript //nologo "%VBS%"

echo.
echo  ╔══════════════════════════════════════════╗
echo  ║  Gremsworth is now alive on your desktop ║
echo  ║                                          ║
echo  ║  - He lives bottom-right corner          ║
echo  ║  - LEFT CLICK   → he talks back          ║
echo  ║  - RIGHT CLICK  → feed / poke / quit     ║
echo  ║  - DRAG         → move him anywhere      ║
echo  ║                                          ║
echo  ║  He will roast you when:                 ║
echo  ║    • You've been idle 10+ min            ║
echo  ║    • CPU or RAM spikes                   ║
echo  ║    • You're up past 1am                  ║
echo  ║    • He feels like it                    ║
echo  ╚══════════════════════════════════════════╝
echo.
pause
