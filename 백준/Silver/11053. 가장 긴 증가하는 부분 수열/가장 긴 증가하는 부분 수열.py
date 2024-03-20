import sys

A = int(sys.stdin.readline())
A_i = list(map(int, sys.stdin.readline().split()))
dp = []
for i, a in enumerate(A_i):
    tmp = [dp[i] for i, v in enumerate(A_i[:i]) if v < a]
    val = max(tmp) if tmp else 0
    dp.append(val + 1)

print(max(dp))