pushd "%~dp0"
{{ python_version }} setup.py sdist
{{ python_version }} setup.py bdist_wheel --universal
pause