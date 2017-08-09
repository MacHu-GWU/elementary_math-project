pushd "%~dp0"
cd ..
cd {{ package_name }}
{{ python_version }} zzz_ezinstall.py
pause