"""
PROBLEM STATEMENT
-----------------
link: https://www.hackerrank.com/challenges/pangrams
"""
import sys


f = sys.stdin
s = f.readline().strip()

unique_chars = set()

for char in s:
    unique_chars.add(char.lower())

for i in range(ord('a'), ord('z') + 1):
    if not chr(i) in unique_chars:
        print("not pangram")
        break
else:
    print("pangram")
