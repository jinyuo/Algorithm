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
    filtered = [i for i in memo if 0 < i < k]
    tmp = [com for com in combinations_with_replacement(filtered, 3) if sum(com) == k]

    print(1 if tmp else 0)