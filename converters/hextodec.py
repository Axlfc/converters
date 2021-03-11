#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sys
def computer(x):
    counter = 0
    numxifra = len(x) - 1
    for c in x:
        c = canviarDigits(c)
        counter = counter + c * 16 ** numxifra
        numxifra = numxifra - 1
    return counter

def canviarDigits(digit):
    if digit == "A" or digit == "a":
        digit = 10
    elif digit == "B" or digit == "b":
        digit = 11
    elif digit == "C" or digit == "c":
        digit = 12
    elif digit == "D" or digit == "d":
        digit = 13
    elif digit == "E" or digit == "e":
        digit = 14
    elif digit == "F" or digit == "f":
        digit = 15
    elif digit >= "0" and digit <= "9":
        digit = int(digit)
    else:
        print("ERROR: hextodec needs hexadecimal characters")
        exit(1)
    return digit

if not sys.stdin.isatty():
    y = sys.stdin.readlines()[0].split(" ")[0].rstrip("\n").lstrip("\n")
    y = computer(y)
    print(y)
    exit(0)

if len(sys.argv) == 1:
    print("ERROR: hextodec needs one argument")
    exit(2)

res = sys.argv[1]
data = computer(res)
print(data)
exit(0)
