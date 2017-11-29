@echo off
:: Check for Python Installation
python --version 2>NUL
if errorlevel 1 goto errorNoPython
echo for installing jinja2 module 
python -m pip install jinja2
echo instllation complete

:: Once done, exit the batch file -- skips executing the errorNoPython section
goto:eof

:errorNoPython
echo Error^: Python not installed