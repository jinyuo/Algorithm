import sys
from itertools import combinations_with_replacement

def memoization(memo, base):
    while memo[-1] < base:
        memo.append(memo[-1] + len(memo))

    return memo

n = int(sys.stdin.readline())
memo = [0]
for i in range(n):
    k = int(sys.stdin.readline())
    memo = memoization(memo, k)
    tmp = [com for com in combinations_with_replacement(memo[1:], 3) if sum(com) == k]

    if tmp:
        print(1)
    else:
        print(0)
