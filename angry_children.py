"""
PROBLEM STATEMENT
-----------------
link: https://www.hackerrank.com/challenges/angry-children-2
"""
n = input()
k = input()
assert 1 <= n <= 10 ** 5
assert 1 <= k <= n

lis = []
for i in range(n):
    lis.append(input())

lis.sort()
sum_lis = []
for i in lis:
    assert 0 <= i <= 10 ** 9

val = 1 - k
answer = 0

sum_lis.append(lis[0])

for i in range(1, n):
    sum_lis.append(sum_lis[i - 1] + lis[i])

for i in range(k):
    answer += val * lis[i]
    val += 2

final_answer = answer
for i in range(k, n):
    new_answer = answer + (k - 1) * lis[i] + (k - 1) * lis[i - k] - 2 * (sum_lis[i - 1] - sum_lis[i - k])
    final_answer = min(new_answer, final_answer)
    answer = new_answer

print final_answer