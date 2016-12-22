""" Ice Cream Parlor
link: https://www.hackerrank.com/challenges/even-tree
"""
import sys

info = []
tree = []
N = None
M = None


def find_children(n):
    children = []
    for x in range(M):
        if edges[x][1] == n:
            children.append(edges[x][0])
            childN = find_children(edges[x][0])
            for child in childN:
                children.append(child)
    return children


def generate_tree():
    global tree
    for x in range(N):
        tree.append([x+1])
    for x in range(N):
        tree[x].append(find_children(x + 1))
    return tree

if __name__ == '__main__':
    global N, M
    f = sys.stdin
    N, M = list(map(int, f.readline().split()))
    edges = []
    for x in range(M):
        u, v = list(map(int, f.readline().split()))
        edges.append([u, v])

    generate_tree()

    count = 0
    for x in range(N):
        if len(tree[x][1]) % 2 == 1:
            count += 1
    print(count - 1)