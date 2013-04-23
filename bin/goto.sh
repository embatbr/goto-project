#!/bin/bash


goto()
{
    ARGS="$@"
    bootstrap_goto.py goto $ARGS
}


goto-label()
{
    ARGS="$@"
    bootstrap_goto.py goto-label $ARGS
}


# goto-list()
# {
#     echo "typed goto-list"
# }