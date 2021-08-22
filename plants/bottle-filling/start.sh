#!/bin/sh

echo "Bottle-filling Factory"
echo "- Starting World View"
./world.py &
echo "- Starting HMI"
./hmi.py &
