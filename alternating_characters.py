"""
PROBLEM STATEMENT
-----------------
link: https://www.hackerrank.com/challenges/alternating-characters
"""
T = int(input())
while T:
    s = input()
    total = 0
    prev = -1
    for char in s:
        if char == prev:
            total += 1
        prev = char
    print(total)
    T -= 1
