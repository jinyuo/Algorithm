from itertools import accumulate

N = int(input().strip())
A = list(map(int, input().split()))
M = int(input().strip())
list_sum = list(accumulate(A, initial=0))

for _ in range(M):
    i, j = map(int, input().split())
    print(list_sum[j] - list_sum[i - 1])