#! /bin/bash -ex

cd "$( dirname "${BASH_SOURCEi[0]}" )"

VENVPATH=../build/venvs/gmxstore_sphinx_venv

# Make the virtualenv not relocatable
mkdir -p ../build/venvs
virtualenv $VENVPATH

source $VENVPATH/bin/activate
cd ../gmxstore && pip install -e .
cd ../docs

pip install sphinx
./pre_gen_docs.sh
sphinx-build -b html -d _build/doctrees . _build/html
