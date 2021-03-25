#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sys

def decto(x, base):
    out = ""
    dicti = generate_dict()
    while x != 0:
        value = x % base
        inv_dicti = {v: k for k, v in dicti.items()}
        out = str(inv_dicti[value]) + out
        x = int(x / base)
    return out

def todec(x, base):
    acum = 0
    dicto = generate_dict()
    max_power = len(x) - 1
    for letter in x:
        if letter in dicto:
            acum += dicto[letter] * base ** max_power
            max_power -= 1
        else:
            print("ERROR: to does not recognize " + letter + " as symbol")
            exit(0)
    return acum


def generate_dict():
    dictio = {}
    # Zero to Nine
    for i in range(10):
        dictio[chr(i + 48)] = i
    # A to Z
    for i in range(26):
        dictio[chr(i + 65)] = i + 10
    # a to z
    for i in range(26):
        dictio[chr(i + 97)] = i + 36
    return dictio


# StdIn processing
if not sys.stdin.isatty():
    arguments = sys.stdin.readlines()[0].rstrip("\n").lstrip("\n").split()
    if len(arguments) == 3:
        # compute
        try:
            if int(arguments[1]) > 61 or int(arguments[2]) > 61:
                print("ERROR: the maximum representable base for to is 61.")
                exit(1)
            else:
                val = todec(arguments[0], int(arguments[1]))
                val = decto(val, int(arguments[2]))
                print(val)
                exit(0)

        except ValueError:
            print("ERROR: to needs an integer representing a base.")
            exit(1)
    elif len(arguments) == 1:
        if len(sys.argv) < 3:
            print("ERROR: to needs two arguments when passing an argument from stdin.")
            exit(1)
        else:
            # compute
            try:
                if int(sys.argv[1]) > 61 or int(sys.argv[2]) > 61:
                    print("ERROR: the maximum representable base for to is 61.")
                    exit(1)
                else:
                    val = todec(arguments[0], int(sys.argv[1]))
                    val = decto(val, int(sys.argv[2]))
                    print(val)
                    exit(0)

            except ValueError:
                print("ERROR: to needs an integer representing a base.")
                exit(1)
    else:
        print("ERROR: to needs three or one arguments in stdin.")
        exit(2)

# Argument processing
if len(sys.argv) < 4:
    print("ERROR: to needs three arguments: magnitude, origin, base.")
    exit(2)

try:
    if int(sys.argv[2]) > 61 or int(sys.argv[3]) > 61:
        print("ERROR: the maximum representable base for to is 61.")
        exit(1)
    else:
        val = todec(sys.argv[1], int(sys.argv[2]))
        val = decto(val, int(sys.argv[3]))
        print(val)
        exit(0)

except ValueError:
    print("ERROR: to needs an integer representing a base.")
    exit(1)

