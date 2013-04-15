#!/bin/bash


goto()
{
    ARGS="$@"
    python3.2 bootstrap_goto.py goto $ARGS
}


goto-label()
{
    echo "typed goto-label"
}


goto-list()
{
    echo "typed goto-list"
}