"""
PROBLEM STATEMENThttps://www.hackerrank.com/challenges/palindrome-index
-----------------
link: https://www.hackerrank.com/challenges/funny-string
"""
import sys


def funny_string(st, li):
    for idx in range(l-1):
        if abs(ord(st[idx])-ord(st[idx+1])) == abs(ord(st[li-idx-1])-ord(st[li-idx-2])):
            pass
        else:
            return "Not Funny"
    return "Funny"


if __name__ == '__main__':
    f = sys.stdin
    T = int(f.readline().strip())
    while T:
        s = f.readline().strip()
        l = len(s)
        print(funny_string(s, l))
        T -= 1
