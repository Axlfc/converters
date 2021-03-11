#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sys
def canviarDigits(num):
    if num == 10:
        num = "A"
    elif num == 11:
        num = "B"
    elif num == 12:
        num = "C"
    elif num == 13:
        num = "D"
    elif num == 14:
        num = "E"
    elif num == 15:
        num = "F"
    elif num >= 0 and num < 10:
        num = str(num)
    else:
        print("ERROR: hextodec needs hexadecimal characters")
        exit(1)
    return num

def DecAlHex(num):
    try:
        dec = int(num)
    except ValueError:
        print("ERROR: dectohex needs decimal characters")
        exit(1)
    hex = ""
    if not dec:
    	print("0")
    	return
    while dec != 0:
        rem = canviarDigits(dec % 16)
        hex = str(rem) + hex
        dec = int(dec / 16)
    print(hex)



try:
    if not sys.stdin.isatty():
        y = sys.stdin.readlines()[0].split(" ")[0].rstrip("\n").lstrip("\n")
        DecAlHex(y)
        exit(0)
except ValueError:
    print("ERROR: dectohex needs decimal characters")
    exit(1)

if len(sys.argv) == 1:
    print("ERROR: dectohex needs one argument")
    exit(2)

DecAlHex(sys.argv[1])