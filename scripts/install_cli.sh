#!/bin/bash
#
# build the package, find the build output, install it with pipx

python3 -m build
ls dist | grep .*.tar.gz | xargs -I % pipx install dist/% --force