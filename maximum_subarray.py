"""
PROBLEM STATEMENT
-----------------
link: https://www.hackerrank.com/challenges/maxsubarray
"""
import sys


def all_non_pos(li):
    for val in li:
        if val > 0:
            return False
        else:
            pass
    return True


if __name__ == '__main__':
    f = sys.stdin

    T = int(f.readline().strip())

    while T:
        N = int(f.readline().strip())
        arr = list(map(int, f.readline().strip().split(' ')))

        max_val = max(arr)
        is_all_non_pos = all_non_pos(arr)

        if is_all_non_pos:
            print("%s %s" % (max_val, max_val))
        else:
            cont_max_sum = 0
            noncont_max_sum = 0
            max_ending_here = max_so_far = 0

            for val in range(1, N+1):
                if arr[val - 1] > 0:
                    noncont_max_sum += arr[val - 1]

            #Kandane's algorith to find maximum subarray
            for x in arr:
                max_ending_here = max(0, max_ending_here + x)
                max_so_far = max(max_so_far, max_ending_here)
            cont_max_sum = max_so_far

            print("%s %s" % (cont_max_sum, noncont_max_sum))
        T -= 1