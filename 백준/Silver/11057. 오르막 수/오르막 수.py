import sys

memo = [[1 for i in range(10)]]
divided = 10007

n = int(sys.stdin.readline())
for i in range(1, n):
    memo.append([sum(memo[-1][i:]) for i in range(10)])
print(sum(memo[-1]) % divided)
