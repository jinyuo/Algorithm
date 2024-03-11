import sys

n = int(sys.stdin.readline().strip())
dp = [[1 for i in range(10)] for j in range(n)]
divided = 1000000000

for i in range(1, n):
    for j in range(0, 10):
        if j == 0:
            dp[i][j] = dp[i - 1][j + 1] % divided
        elif j == 9:
            dp[i][j] = dp[i - 1][j - 1] % divided
        else:
            dp[i][j] = (dp[i - 1][j - 1] + dp[i - 1][j + 1]) % divided

print(sum(dp[-1][1:]) % divided)