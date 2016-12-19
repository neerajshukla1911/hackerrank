"""
PROBLEM STATEMENT
-----------------
link: https://www.hackerrank.com/challenges/making-anagrams
"""

def build_map(s):
    the_map = {}
    for char in s:
        if char not in the_map:
            the_map[char] = 1
        else:
            the_map[char] += 1

    return the_map
