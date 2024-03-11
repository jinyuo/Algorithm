import sys

N, M = map(int, sys.stdin.readline().split())
miro = [list(map(int, sys.stdin.readline().split())) for i in range(N)]
dp = [[0 for j in range(M)] for i in range(N)]

for i in range(N):
    for j in range(M):
        if i == 0 and j == 0:
            val = miro[i][j]
        elif i == 0:
            val = dp[i][j - 1] + miro[i][j]
        elif j == 0:
            val = dp[i - 1][j] + miro[i][j]
        else:
            val = max(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + miro[i][j]
        dp[i][j] = val

print(dp[i][j])