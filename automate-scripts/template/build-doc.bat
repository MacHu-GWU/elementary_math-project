pushd "%~dp0"
cd {{ package_name }}
{{ python_version }} zzz_manual_install.py
cd ..
{{ python_version }} create_doctree.py
make html