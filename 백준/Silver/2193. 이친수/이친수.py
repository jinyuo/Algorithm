import sys

N = int(sys.stdin.readline())
dp = [[0, 1]]
for i in range(1, N):
    dp.append([dp[-1][0] + dp[-1][1], dp[-1][0]])

print(sum(dp[-1]))