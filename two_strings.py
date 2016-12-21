"""
PROBLEM STATEMENT
-----------------
link: https://www.hackerrank.com/challenges/common-child
"""
import sys


def lcs_len(s1, s2):
    prev_lcs = [0] * (len(s2) + 1)
    curr_lcs = [0] * (len(s2) + 1)
    for c1 in s1:
        curr_lcs, prev_lcs = prev_lcs, curr_lcs
        for j, c2 in enumerate(s2, 1):
            curr_lcs[j] = (
                1 + prev_lcs[j - 1] if c1 == c2 else
                max(prev_lcs[j], curr_lcs[j - 1])
            )
    return curr_lcs[-1]


def main():
    f = sys.stdin

    s1 = f.readline().strip()
    s2 = f.readline().strip()
    print(lcs_len(s1, s2))


if __name__ == '__main__':
    main()
