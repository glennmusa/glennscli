#!/bin/bash
#
# install the required dependencies for development and test and activate a virtual env

python3 -m venv .venv
. .venv/bin/activate
pip3 install -e . && pip install -e .[test_dependencies]