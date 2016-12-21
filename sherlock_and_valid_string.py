"""
PROBLEM STATEMENT
-----------------
link: https://www.hackerrank.com/challenges/sherlock-and-valid-string
"""
from collections import Counter
import sys


def is_valid(str):
    char_map = Counter(str)
    char_occurence_map = Counter(char_map.values())

    if len(char_occurence_map) == 1:
        return True

    if len(char_occurence_map) == 2:
        for v in char_occurence_map.values():
            if v == 1:
                return True

    return False

f = sys.stdin

s = f.readline().strip()
if is_valid(s):
    print("YES")
else:
    print("NO")