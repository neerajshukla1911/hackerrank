"""
PROBLEM STATEMENT
-----------------
link: https://www.hackerrank.com/challenges/sherlock-and-cost
"""
import sys


class Solution(object):
    def solve(self, cipher):
        B = cipher
        N = len(B)
        dp = [[0, 0] for _ in xrange(N + 1)]

        LOW = 0
        HIGH = 1
        for i in xrange(2, N + 1):
            dp[i][LOW] = max(dp[i - 1][LOW], dp[i - 1][HIGH] + abs(1 - B[i - 2]))
            dp[i][HIGH] = max(dp[i - 1][HIGH], dp[i - 1][LOW] + abs(B[i - 1] - 1))

        return str(max(dp[-1][LOW], dp[-1][HIGH]))


if __name__ == "__main__":
    f = sys.stdin
    testcases = int(f.readline().strip())

    for t in xrange(testcases):
        # construct cipher
        N = int(f.readline().strip())
        cipher = map(int, f.readline().strip().split(' '))

        # solve
        s = "%s\n" % (Solution().solve(cipher))
        print s,
