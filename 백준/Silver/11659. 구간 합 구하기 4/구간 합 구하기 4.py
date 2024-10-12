import sys
from itertools import accumulate

N, M = map(int, sys.stdin.readline().split())
list_num = list(map(int, sys.stdin.readline().split()))
list_subsum = list(accumulate(list_num, initial=0))
for _ in range(M):
    i, j = map(int, sys.stdin.readline().split())
    print(list_subsum[j] - list_subsum[i - 1])