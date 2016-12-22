import sys

f = sys.stdin

V = int(f.readline().strip())
n = int(f.readline().strip())
arr = list(map(int, f.readline().strip().split()))

for i in range(n):
    if arr[i]==V:
        print(i)
        break