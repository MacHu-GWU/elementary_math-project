pushd "%~dp0"
python setup.py sdist
python setup.py bdist_wheel --universal
pause