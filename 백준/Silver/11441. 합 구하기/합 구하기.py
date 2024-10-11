N = int(input().strip())
A = list(map(int, input().split()))
M = int(input().strip())
list_sum = [0 for _ in range(N + 1)]
for i in range(1, N + 1):
    list_sum[i] = list_sum[i - 1] + A[i - 1]

for _ in range(M):
    i, j = map(int, input().split())
    print(list_sum[j] - list_sum[i - 1])
