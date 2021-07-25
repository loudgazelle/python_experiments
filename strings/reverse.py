#!/usr/local/bin/python3
import sys

if len(sys.argv) <= 1: 
  # no string provided, print usage
  print("usage: reverse.py <'string in quotes'>")
  exit(1)
else:
  # take the first argument and reverse it
  print(sys.argv[1][::-1])
  exit(0)