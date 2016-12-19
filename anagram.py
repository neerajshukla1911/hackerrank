"""
PROBLEM STATEMENT
-----------------
link: https://www.hackerrank.com/challenges/anagram
"""
import sys


def build_map(s):
    the_map = {}
    for char in s:
        if char not in the_map:
            the_map[char] = 1
        else:
            the_map[char] +=1
             
    return the_map       
     
 
def cost_to_make_anagram(s1, s2):
    map1 = build_map(s1)
    map2 = build_map(s2)

    count = 0
    for key in map2.keys():
        if key not in map1:
            count += map2[key]
        else:
            count += max(0, map2[key]-map1[key])

    for key in map1.keys():
        if key not in map2:
            count += map1[key]
        else:
            count += max(0, map1[key]-map2[key])

    return count

if __name__ == '__main__':
    f = sys.stdin
    s1 = f.readline().strip()
    s2 = f.readline().strip()

    print(cost_to_make_anagram(s1, s2))
