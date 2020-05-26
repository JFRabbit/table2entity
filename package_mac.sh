#!/usr/bin/env bash

./venv/bin/pyinstaller \
--onefile --add-binary='/System/Library/Frameworks/Tk.framework/Tk':'tk' \
--add-binary='/System/Library/Frameworks/Tcl.framework/Tcl':'tcl' \
-F ./table_to_entity/tte.py --clean

mkdir ./dist/config/
cp -rf ./config_template/config.yaml ./dist/config/
cp README.md ./dist/
