""" Ice Cream Parlor
https://www.hackerrank.com/monthly/challenges/icecream-parlor
"""
import sys
from itertools import combinations

f = sys.stdin

T = int(f.readline().strip())

while T:
    dollars = int(f.readline().strip())
    total_flavors = int(f.readline().strip())  # unused variable
    flavors_costs = f.readline()
    flavors_costs = [int(x) for x in flavors_costs.split(' ')]

    flavors_combinations = combinations(flavors_costs, 2)

    for flavors_tuple in flavors_combinations:
        if ((flavors_tuple[0] + flavors_tuple[1]) == dollars):
            first_flavor = flavors_costs.index(flavors_tuple[0])

            second_flavor = flavors_costs.index(flavors_tuple[1],
                                                first_flavor + 1)

            print("{} {}".format(first_flavor + 1, second_flavor + 1))
            break
    T -= 1