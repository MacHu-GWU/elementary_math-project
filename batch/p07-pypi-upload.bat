REM cd to repository directory
pushd "%~dp0"
cd ..

CHOICE /C YN /M "upload to pypi, Y to continue, N to cancle"
IF ERRORLEVEL==2 goto end
IF ERRORLEVEL==1 goto upload

:upload
twine upload dist/* -r pypi
goto end

:end
pause