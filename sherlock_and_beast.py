""" Ice Cream Parlor
https://www.hackerrank.com/challenges/sherlock-and-the-beast
"""
import sys


def sherlock_and_beast(N):
    if (N < 3):
        return "-1"
    three_cnt = N // 3
    five_cnt = 0
    while three_cnt >= 0:
        rem = N - three_cnt * 3
        if rem % 5 == 0:
            five_cnt = rem // 5
            break
        three_cnt -= 1

    if three_cnt <= 0 and five_cnt == 0:
        return "-1"

    return "555" * three_cnt + "33333" * five_cnt


if __name__ == '__main__':
    f = sys.stdin
    T = int(f.readline().strip())
    while T:
        n = int(f.readline().strip())
        print(sherlock_and_beast(n))
        T -= 1