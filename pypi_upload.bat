pushd "%~dp0"
CHOICE /C YN /M "upload to pypi, Y to continue, N to cancle"
IF ERRORLEVEL==2 goto end
IF ERRORLEVEL==1 goto upload

:upload
python setup.py sdist upload -r pypi
goto end

:end
pause