@echo off
title Antivirus
echo Antivirus
echo created by Rituraj Gupta
:start
IF EXIST virus.bat goto infected
IF NOT EXIST virus.bat goto clean
cd C:Windowssystem32
:infected
echo Virus Detected
del virus.bat
pause goto start
:clean
echo System Secured
pause
exit