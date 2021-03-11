#!/usr/bin/env python3
import sys
if not sys.stdin.isatty():
	y = sys.stdin.readlines()[0].split(" ")[0].rstrip("\n").lstrip("\n")
	try:
		y = chr(int(y))
		print(y)
		exit(0)
	except ValueError:
		print("ERROR: dectoutf needs decimal numbers")
		exit(1)


if len(sys.argv) == 1:
	print("ERROR: dectoutf needs one argument")
	exit(2)

res = sys.argv[1]
try:
	data = chr(int(res))
except ValueError:
	print("ERROR: dectoutf needs decimal numbers")
	exit(1)
print(data)
exit(0)
