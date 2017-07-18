REM cd to repository directory
pushd "%~dp0"
cd ..

REM source code distribute, usually a .tar.gz file
{{ python_version }} setup.py sdist

REM
{{ python_version }} setup.py bdist_wheel --universal

pause