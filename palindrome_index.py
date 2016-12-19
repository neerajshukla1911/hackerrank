"""
PROBLEM STATEMENThttps://www.hackerrank.com/challenges/palindrome-index
-----------------
link: https://www.hackerrank.com/challenges/palindrome-index
"""
import sys
f = sys.stdin
T = int(f.readline().strip())
while T:
    difference = lambda x, y: abs(ord(x) - ord(y))
    s = f.readline().strip()
    idx = -1
    mid = len(s) // 2
    l = zip(s, reversed(s))
    for i in range(0, mid):
        d = difference(l[i][0], l[i][1])
        if d > 0:
            idx = i
            break
    print idx
    T -= 1
