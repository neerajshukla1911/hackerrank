"""
PROBLEM STATEMENT
------------------
Two kingdoms are at war. Kingdom 1 has N soldiers (numbered as 1 to N) and the war goes on for K days. Each day only one soldier from each kingdom fights.

Kingdom 1 can select one soldier from soldier number Ni to Nj. Ni and Nj are provided to you for each day.

Selection criteria: Each soldier has 2 parameters - A & B. A soldier is/are selected if A is max. If more than one soldier has A max then the soldier with min. B (of the shortlisted soldiers) is/are selected. If more than one soldier is still available, then the soldier with least index (of the shortlisted soldiers) is selected.

Print the soldier number selected for each day of the war.

Input:
Line 1 contains number of soldiers of Kingdom1 => N
Line 2 contains N space-separated values of A
Line 3 contains N space-separated values of B
Line 4 contains number of days fight goes on => K
Next K lines contain space separated values of Ni and Nj

Output:
K lines contain soldier number selected for each day of the war.

Sample Input:
10
2 5 3 7 9 2 9 8 7 15
5 2 1 8 3 1 2 9 0 5
3
1 5
3 8
4 10

Result:
5
7
10

"""
import sys


def find_all_max_val_indexes(li):
    '''
    finds all occurances of max in given list
    '''
    max_val_indexes = [0]
    for idx, val in enumerate(li[1:], start=1):
        if val > li[max_val_indexes[0]]:
            max_val_indexes = [idx]
        elif val == li[max_val_indexes[0]]:
            max_val_indexes.append(idx)
    return max_val_indexes


def find_all_min_val_indexes_with_second_min(li):
    '''
    finds all occurances of min, and index of second min in given list
    '''

    min_val_indexes = [0]
    second_min_index = 1

    for idx, val in enumerate(li[1:], start=1):

        if li[min_val_indexes[0]] < val < li[second_min_index]:
            second_min_index = idx
        elif li[second_min_index] < li[min_val_indexes[0]]:
            second_min_index = min_val_indexes[0]
        elif val < li[min_val_indexes[0]] < li[second_min_index]:
            second_min_index = min_val_indexes[0]

        if val < li[min_val_indexes[0]]:
            min_val_indexes = [idx]
        elif val == li[min_val_indexes[0]]:
            min_val_indexes.append(idx)
    return min_val_indexes, second_min_index


if __name__ == '__main__':
    f = sys.stdin
    N = int(f.readline().strip())
    A = map(int, f.readline().strip().split(' '))
    B = map(int, f.readline().strip().split(' '))
    K = int(f.readline().strip())
    for val in xrange(K):
        ninj = map(int, f.readline().strip().split(' '))
        max_indexes = find_all_max_val_indexes(A[ninj[0]-1:ninj[1]])
        if len(max_indexes)>1:
            min_indexes, second_min_index = find_all_min_val_indexes_with_second_min(B[ninj[0] - 1:ninj[1]])
            if len(min_indexes)>1:
                print second_min_index + ninj[0]
            else:
                print min_indexes[0] + ninj[0]
        else:
            print max_indexes[0] + ninj[0]
