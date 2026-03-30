@ECHO OFF & CLS & ECHO.
NET FILE 1>NUL 2>NUL & IF ERRORLEVEL 1 (ECHO Error: run this script as Administrator & ECHO. & PAUSE & EXIT /D)

echo [1] Stopping servers...
net stop ews-dashboard > nul
net stop ews-dbserver > nul
net stop ews-httpserver > nul

echo [2] Deploying application's files...
for %%d in (A B C D E F G H I J K L M N O P Q R S T U V W X Y Z) do (
	if exist "%%d:\challenges\EasyPHP-Webserver-14.1b2.7z" (
		"C:\Program Files\7-Zip\7z.exe" x %%d:\challenges\EasyPHP-Webserver-14.1b2.7z -o"C:\Program Files (x86)\" -aoa > nul
		goto done
	)
)

echo ERROR: Archive file not found. Did you mount the encrypted container?
pause
exit

:done

echo [3] Starting back servers...
net start ews-dashboard
net start ews-dbserver
net start ews-httpserver

echo [4] Modifying C:\Windows\System32\drivers\etc\hosts file with the right entry.

for /f "delims=[] tokens=2" %%a in ('ping -4 -n 1 %ComputerName% ^| findstr [') do set vmip=%%a
echo Found VM IP: %vmip%

findstr /V e-commune.org C:\Windows\System32\drivers\etc\hosts > C:\Windows\System32\drivers\etc\hosts.deploy.bak
copy /Y C:\Windows\System32\drivers\etc\hosts.deploy.bak C:\Windows\System32\drivers\etc\hosts > nul
echo %vmip% www.e-commune.org >> C:\Windows\System32\drivers\etc\hosts

echo *
echo **
echo ****
echo *****
echo ******
echo *******
echo ********
echo *********
echo **********
echo ***********
echo [6] Done! You can close this window :)
pause
