@REM ---- Windows batch portion ----
@echo off
setlocal

REM Find Git Bash on Windows to run the real hook script
where bash >nul 2>nul
if %ERRORLEVEL% EQU 0 (
    bash "%~dp0%~1" %2 %3 %4 %5 %6 %7 %8 %9
    exit /b %ERRORLEVEL%
)

for %%G in (
    "%ProgramFiles%\Git\bin\bash.exe"
    "%ProgramFiles(x86)%\Git\bin\bash.exe"
    "%LOCALAPPDATA%\Programs\Git\bin\bash.exe"
) do (
    if exist %%G (
        %%G "%~dp0%~1" %2 %3 %4 %5 %6 %7 %8 %9
        exit /b %ERRORLEVEL%
    )
)

echo timeln-skills: bash not found. Install Git for Windows. >&2
exit /b 1

REM ---- Unix shell portion (this file is a polyglot) ----
: <<'BATCH_END'
BATCH_END
#!/usr/bin/env bash
exec "$(dirname "$0")/$1" "${@:2}"
