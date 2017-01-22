#!/bin/bash

source ./venv/*/activate

exec python tats.py $@

deactivate
