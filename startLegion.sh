#!/bin/bash

echo "Strap yourself in, we're starting Legion..."

# Set everything we might need as executable
chmod a+x -R ./deps/*
chmod a+x -R ./scripts/*

# Determine and set the Python and Pip paths
source ./deps/detectPython.sh

# Determine OS, version and if WSL
source ./deps/detectOs.sh

# Figure if fist run or recloned and install deps 
if [ ! -f ".initialized" ] | [ -f ".justcloned" ]
then
    echo "First run here (or you did a pull to update). Let's try to automatically install all the dependancies..."
    if [ ! -d "tmp" ]
    then
        mkdir tmp
    fi
    echo "Running ${DEPINSTALLER}..."
    bash ./deps/${DEPINSTALLER}
    # Determine if additional Sparta scripts are installed
    bash ./deps/detectScripts.sh
    source ./deps/detectPython.sh
    touch .initialized
    rm .justcloned -f
fi

export QT_XCB_NATIVE_PAINTING=0
export QT_AUTO_SCREEN_SCALE_FACTOR=1.5

if [[ $1 != 'setup' ]]
then
    /usr/bin/env python3 legion.py
fi
