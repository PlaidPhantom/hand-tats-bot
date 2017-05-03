#!/bin/bash

source ./venv/*/activate

exec python tats.py $@ 2>&1 >> tats.log

deactivate
