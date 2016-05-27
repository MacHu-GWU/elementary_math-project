pushd "%~dp0"
cd elementary_math
python zzz_manual_install.py
cd ..
python create_doctree.py
make html