#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sys


def compute(x):
    counter = 0
    numxifra = len(x) - 1
    for c in x:
        if c == '0' or c == '1':
            c = int(c)
            counter = counter + c * 2 ** numxifra
            numxifra = numxifra - 1
        else:
            print("ERROR: bintodec needs binary characters")
            exit(1)
    return counter


# StdIn processing
if not sys.stdin.isatty():
    y = sys.stdin.readlines()[0].split(" ")[0].rstrip("\n").lstrip("\n")
    y = compute(y)
    print(y)
    exit(0)

# Argument processing
if len(sys.argv) == 1:
    print("ERROR: bintodec needs one argument")
    exit(2)

y = compute(sys.argv[1])
print(y)
exit(0)


