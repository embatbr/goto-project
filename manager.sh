#!/bin/bash

rm -Rf bin/__pycache__ goto/__pycache__
clear

./tests/goto.py "$@"

rm -Rf bin/__pycache__ goto/__pycache__
