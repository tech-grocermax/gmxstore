#! /bin/bash -ex

cd "$( dirname "${BASH_SOURCEi[0]}" )"

pandoc -f markdown -t rst ../README.md -o ../README.rst
