#!/bin/bash

source ./venv/*/activate

exec python3 tats.py $@

deactivate
