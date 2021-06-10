#!/bin/bash
# on ubuntu 20.04
# to make it work: https://packaging.python.org/tutorials/packaging-projects/

rm -rf build dist
python3 -m build
python3 -m twine upload --repository testpypi dist/*
python3 -m pip install --index-url https://test.pypi.org/simple/ --no-deps pyperplot --upgrade
