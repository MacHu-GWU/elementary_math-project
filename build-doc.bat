pushd "%~dp0"
cd elementary_math
python34 zzz_manual_install.py
cd ..
python34 create_doctree.py
make html