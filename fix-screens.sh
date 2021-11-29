#!/bin/sh
cd "$(dirname "$0")"
./align-screens.py --hz=60
sleep 5
./align-screens.py
