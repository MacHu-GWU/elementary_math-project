REM cd to repository directory
pushd "%~dp0"
cd ..

REM source code distribute, usually a .tar.gz file
python34 setup.py sdist

REM
python34 setup.py bdist_wheel --universal

pause