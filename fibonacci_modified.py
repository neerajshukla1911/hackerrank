"""
PROBLEM STATEMENT
-----------------
link: https://www.hackerrank.com/challenges/fibonacci-modified
"""
import sys

f = sys.stdin
t1, t2, tn = list(map(int, f.readline().strip().split(' ')))

output = 0
for idx in range(tn-2):
    output = t1 + t2*t2
    t1 = t2
    t2 = output

print(output)

