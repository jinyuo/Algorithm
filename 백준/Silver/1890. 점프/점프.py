import sys

N = int(sys.stdin.readline())
game = [list(map(int, sys.stdin.readline().strip().split())) for i in range(N)]
dp = [[0 for _ in range(N)] for _ in range(N)]

for i in range(N):
    for j in range(N):
        if i == 0 and j == 0:
            dp[i][j] = 1
        if dp[i][j] > 0 and game[i][j] > 0:
            if i + game[i][j] < N:
                dp[i + game[i][j]][j] += dp[i][j]
            if j + game[i][j] < N:
                dp[i][j + game[i][j]] += dp[i][j]
print(dp[N - 1][N - 1])