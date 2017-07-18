REM cd to repository directory
pushd "%~dp0"
cd ..

REM install the package
cd elementary_math
python34 zzz_manual_install.py

REM create doc tree
cd ..
cd batch
python34 create_doctree.py

REM build html doc
cd ..

make html

echo Complete!

pause