#!/bin/bash


function goto()
{
    ARGS="$@"
    ./bootstrap.py goto $ARGS
    echo $RET
}

goto
