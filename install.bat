@echo off
REM ========================================
REM    ZenLang Complete Installation
REM ========================================

echo.
echo ========================================
echo    ZenLang Installation
echo ========================================
echo.

REM Check Python installation
python --version >nul 2>&1
if errorlevel 1 (
    echo [ERROR] Python is not installed or not in PATH
    echo.
    echo Please install Python 3.7+ from https://www.python.org/
    echo.
    pause
    exit /b 1
)

echo [OK] Python found
python --version
echo.

REM Get the directory where this script is located
set "ROOT_DIR=%~dp0"
set "ROOT_DIR=%ROOT_DIR:~0,-1%"
set "ZENLANG_DIR=%ROOT_DIR%\zenlang"

echo Installing ZenLang from: %ROOT_DIR%
echo ZenLang directory: %ZENLANG_DIR%
echo.

REM Check if zenlang directory exists
if not exist "%ZENLANG_DIR%" (
    echo [ERROR] zenlang directory not found!
    echo Expected at: %ZENLANG_DIR%
    pause
    exit /b 1
)

REM Create zen.bat in root directory
echo Creating zen.bat launcher in root...
(
echo @echo off
echo python "%%~dp0zenlang\cli\zen.py" %%*
) > "%ROOT_DIR%\zen.bat"

if exist "%ROOT_DIR%\zen.bat" (
    echo [OK] zen.bat created in root directory
) else (
    echo [ERROR] Failed to create zen.bat
    pause
    exit /b 1
)

REM Also create zen.bat inside zenlang directory for direct access
echo Creating zen.bat inside zenlang directory...
(
echo @echo off
echo python "%%~dp0cli\zen.py" %%*
) > "%ZENLANG_DIR%\zen.bat"

if exist "%ZENLANG_DIR%\zen.bat" (
    echo [OK] zen.bat created in zenlang directory
) else (
    echo [WARNING] Failed to create zen.bat in zenlang directory
)

REM Test installation
echo.
echo Testing installation...
"%ROOT_DIR%\zen.bat" version >nul 2>&1
if errorlevel 1 (
    echo [WARNING] zen command test failed
    echo Trying alternative test...
    python "%ZENLANG_DIR%\cli\zen.py" version
) else (
    echo [OK] zen command works!
    "%ROOT_DIR%\zen.bat" version
)

REM Add to PATH
echo.
echo ========================================
echo    PATH Configuration
echo ========================================
echo.

REM Check if already in PATH
echo %PATH% | find /i "%ROOT_DIR%" >nul
if errorlevel 1 (
    echo ZenLang is not in your PATH.
    echo.
    echo Choose an option:
    echo   1. Add to PATH automatically (requires restart)
    echo   2. Show manual instructions
    echo   3. Skip PATH setup
    echo.
    set /p PATH_CHOICE="Enter choice (1-3): "
    
    if "!PATH_CHOICE!"=="1" (
        echo.
        echo Adding to PATH...
        setx PATH "%PATH%;%ROOT_DIR%" >nul 2>&1
        if errorlevel 1 (
            echo [WARNING] Failed to add to PATH automatically
            echo Please add manually: %ROOT_DIR%
        ) else (
            echo [OK] Added to PATH
            echo IMPORTANT: You must restart your terminal for PATH changes to take effect
        )
    ) else if "!PATH_CHOICE!"=="2" (
        echo.
        echo Manual PATH Setup:
        echo 1. Press Windows + X and select "System"
        echo 2. Click "Advanced system settings"
        echo 3. Click "Environment Variables"
        echo 4. Under "User variables", select "Path" and click "Edit"
        echo 5. Click "New" and add: %ROOT_DIR%
        echo 6. Click "OK" on all dialogs
        echo 7. Restart your terminal
    )
) else (
    echo [OK] ZenLang is already in PATH
)

REM Clean up old files
echo.
echo ========================================
echo    Cleanup
echo ========================================
echo.

echo Removing old/redundant files...

if exist "%ROOT_DIR%\setup.bat" (
    del "%ROOT_DIR%\setup.bat" >nul 2>&1
    echo [OK] Removed setup.bat
)

if exist "%ROOT_DIR%\test_zen.bat" (
    del "%ROOT_DIR%\test_zen.bat" >nul 2>&1
    echo [OK] Removed test_zen.bat
)

if exist "%ROOT_DIR%\GET_STARTED.md" (
    del "%ROOT_DIR%\GET_STARTED.md" >nul 2>&1
    echo [OK] Removed GET_STARTED.md
)

if exist "%ROOT_DIR%\SETUP_ICONS.txt" (
    del "%ROOT_DIR%\SETUP_ICONS.txt" >nul 2>&1
    echo [OK] Removed SETUP_ICONS.txt
)

REM VSCode Extension (optional)
echo.
echo ========================================
echo    VSCode Extension (Optional)
echo ========================================
echo.

if exist "%ZENLANG_DIR%\vscode-extension" (
    echo VSCode extension files found.
    echo.
    set /p INSTALL_VSCODE="Install VSCode extension? (y/n): "
    if /i "!INSTALL_VSCODE!"=="y" (
        echo.
        echo To install the VSCode extension:
        echo 1. Open VSCode
        echo 2. Press Ctrl+Shift+P
        echo 3. Type "Extensions: Install from VSIX"
        echo 4. Navigate to: %ZENLANG_DIR%\vscode-extension
        echo.
        echo OR run PowerShell command:
        echo   cd "%ZENLANG_DIR%\vscode-extension"
        echo   .\install.ps1
        echo.
    )
) else (
    echo VSCode extension not found (optional)
)

REM Create desktop shortcut (optional)
echo.
set /p CREATE_SHORTCUT="Create desktop shortcut? (y/n): "
if /i "%CREATE_SHORTCUT%"=="y" (
    echo Creating desktop shortcut...
    
    set "SHORTCUT=%USERPROFILE%\Desktop\ZenLang.lnk"
    powershell -Command "$WS = New-Object -ComObject WScript.Shell; $SC = $WS.CreateShortcut('%SHORTCUT%'); $SC.TargetPath = 'cmd.exe'; $SC.Arguments = '/k cd /d \"%ROOT_DIR%\" ^&^& echo ZenLang Environment ^&^& echo Type: zen help'; $SC.WorkingDirectory = '%ROOT_DIR%'; $SC.Save()" >nul 2>&1
    
    if exist "%SHORTCUT%" (
        echo [OK] Desktop shortcut created
    ) else (
        echo [WARNING] Failed to create shortcut
    )
)

REM Installation complete
echo.
echo ========================================
echo    Installation Complete!
echo ========================================
echo.
echo ZenLang is installed at: %ROOT_DIR%
echo.
echo Quick Start Commands:
echo   zen help                              Show all commands
echo   zen version                           Show version
echo   zen run zenlang\examples\main.zen     Run example
echo   zen run zenlang\examples\simple_web_server.zen    Start web server
echo.
echo Documentation:
echo   %ZENLANG_DIR%\GUIDE.md               Complete guide
echo   %ZENLANG_DIR%\README.md              Overview
echo   %ZENLANG_DIR%\GETTING_STARTED.txt    Quick reference
echo.
echo Examples:
echo   %ZENLANG_DIR%\examples\              All example programs
echo.
echo If 'zen' command is not found:
echo   1. Restart your terminal/command prompt
echo   2. Or use full path: %ROOT_DIR%\zen.bat
echo   3. Or add %ROOT_DIR% to PATH manually
echo.

pause
