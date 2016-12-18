#!/bin/python
"""
PROBLEM STATEMENT
-----------------
link: https://www.hackerrank.com/challenges/the-love-letter-mystery

"""
import sys


f = sys.stdin
n = int(f.readline().strip())
B = list(map(int, list(f.readline().strip())))

count = 0
for i in range(2,n):
    if B[i-2] == 0 and B[i-1] == 1 and B[i] == 0:
        B[i] = 1
        count += 1
print(count)
