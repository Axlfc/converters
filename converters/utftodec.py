#!/usr/bin/env python3
import sys
if not sys.stdin.isatty():
	y = sys.stdin.readlines()[0].split(" ")[0].rstrip("\n").lstrip("\n")
	y = ord(y)
	print(y)
	exit(0)

if len(sys.argv) == 1:
	print("ERROR: utftodec needs one argument")
	exit(2)

res = sys.argv[1]
data = ord(res)
print(data)
exit(0)
