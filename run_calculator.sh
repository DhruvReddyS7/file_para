#!/bin/sh

PROGRAM_FILE=$1
A=$2
B=$3

if [ "$PROGRAM_FILE" = "Calculator.java" ]; then
  javac Calculator.java && java Calculator $A $B
else
  python3 calculator.py $A $B
fi
