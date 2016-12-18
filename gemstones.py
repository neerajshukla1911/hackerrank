#!/usr/bin/py
"""
PROBLEM STATEMENT
-----------------
link: https://www.hackerrank.com/challenges/gem-stones
"""
import sys

f = sys.stdin

N = int(f.readline().strip())
s = set(f.readline().strip())

while N > 1:
    s &= set(f.readline().strip())
    N -= 1

print(len(s))
