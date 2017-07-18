REM cd to repository directory
pushd "%~dp0"
cd ..

REM install the package
cd {{ package_name }}
{{ python_version }} zzz_manual_install.py

REM create doc tree
cd ..
cd batch
{{ python_version }} create_doctree.py

REM build html doc
cd ..

make html

echo Complete!

pause