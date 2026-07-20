#!/bin/bash
# Deps (pytest, pytest-json-ctrf) are already in the environment image.
# Do not use `set -e` here: a failing pytest must still write reward.txt.

mkdir -p /logs/verifier

pytest /tests/test_outputs.py -rA --ctrf /logs/verifier/ctrf.json

if [ $? -eq 0 ]; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi
