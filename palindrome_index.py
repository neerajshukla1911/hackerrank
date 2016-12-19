"""
PROBLEM STATEMENThttps://www.hackerrank.com/challenges/palindrome-index
-----------------
link: https://www.hackerrank.com/challenges/palindrome-index
"""
import sys


def is_palindrome(s):
    for idx in range(len(s) // 2):
        if s[idx] != s[len(s) - idx - 1]:
            return False
    return True


def palindrome_index(s):
    for idx in range((len(s) + 1) // 2):
        if s[idx] != s[len(s) - idx - 1]:
            if is_palindrome(s[:idx] + s[idx + 1:]):
                return idx
            else:
                return len(s) - idx - 1
    return -1


if __name__ == '__main__':
    f = sys.stdin
    T = int(f.readline())
    while T:
        s = f.readline()
        print(palindrome_index(s))
        T -= 1
