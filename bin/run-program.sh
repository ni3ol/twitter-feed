#!/bin/sh

set -ex

export PYTHONPATH=$(pwd)/src
exec python src/main.py $1 $2
