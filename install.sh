#!/usr/bin/env bash
pip -V
pip install -U pip -i http://mirrors.aliyun.com/pypi/simple/
pip install -r requirements.txt -i http://mirrors.aliyun.com/pypi/simple/
pip uninstall -y setuptools
pip install -U setuptools==44.0.0