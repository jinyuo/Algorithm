from itertools import accumulate
import sys

N = int(sys.stdin.readline().strip())
A = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline().strip())
list_sum = list(accumulate(A, initial=0))

for _ in range(M):
    i, j = map(int, sys.stdin.readline().split())
    print(list_sum[j] - list_sum[i - 1])