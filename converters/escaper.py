#!/usr/bin/python3
# -*- coding: utf-8 -*-
import re
import sys

def compute(x):
    metachars = "\\)(']^[|+\"-{$}"
    print(metachars)
    for char in metachars:
        x = x.replace(char, "\\" + char)
    return x


# StdIn processing
if not sys.stdin.isatty():
    y = sys.stdin.readlines()[0].split(" ")[0].rstrip("\n").lstrip("\n")
    y = compute(y)
    print(y)
    exit(0)

# Argument processing
if len(sys.argv) == 1:
    print("ERROR: escaper needs one argument")
    exit(2)

y = compute(sys.argv[1])
print(y)
exit(0)


