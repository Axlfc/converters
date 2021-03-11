#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sys


def compute(x):
    try:
        x = int(x)
    except:
        print("ERROR: dectobin needs decimal characters")
        exit(1)


    bin = ""
    if not x:
        return x
    while x != 0:
        bin = str(x % 2) + bin
        x = int(x / 2)

    return bin


# StdIn processing
if not sys.stdin.isatty():
    y = sys.stdin.readlines()[0].split(" ")[0].rstrip("\n").lstrip("\n")
    y = compute(y)
    print(y)
    exit(0)

# Argument processing
if len(sys.argv) == 1:
    print("ERROR: dectobin needs one argument")
    exit(2)

y = compute(sys.argv[1])
print(y)
exit(0)
