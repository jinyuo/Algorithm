import sys

N = int(sys.stdin.readline())
stairs = [int(sys.stdin.readline()) for _ in range(N)]
dp = []
for i in range(N):
    if i == 0:
        tmp = [0, 0]
    elif i == 1:
        tmp = [0, stairs[0]]
    else:
        tmp = [max(dp[-2])] + dp[-1][:-1]
    dp.append([t + stairs[i] for t in tmp])
print(max(dp[-1]))