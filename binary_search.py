"""
PROBLEM STATEMENT
-----------------
link: https://www.hackerrank.com/challenges/tutorial-intro
"""
import sys

f = sys.stdin
V = int(f.readline().strip())
n = int(f.readline().strip())
arr = map(int, f.readline().strip().split(' '))

low = 0
high = n-1
for i, val in enumerate(arr):
    mid = (low + high-1)/2
    if val == V:
        print(i)
        sys.exit()
    elif val > V:
        low = mid
    else:
        high = mid-1