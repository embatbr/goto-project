#!/bin/bash


goto()
{
    ARGS="$@"
    bootstrap_goto.py goto $ARGS

    if [ "$?" = "0" ]; then
        if [ -f /tmp/goto ]; then
            DIR=$(head -1 /tmp/goto)
            $DIR
            rm /tmp/goto
        fi
    fi
}


label()
{
    ARGS="$@"
    bootstrap_goto.py goto-label $ARGS
}