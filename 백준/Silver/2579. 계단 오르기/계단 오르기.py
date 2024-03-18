import sys

N = int(sys.stdin.readline())
stairs = [int(sys.stdin.readline()) for _ in range(N)]
dp = []

for i in range(N):
    if i == 0:
        tmp = [0, stairs[0]]
    elif i == 1:
        tmp = [stairs[1], stairs[0] + stairs[1]]
    else:
        tmp = [max(dp[-2]) + stairs[i]] + [v + stairs[i] for v in dp[-1][:-1]]
    dp.append(tmp)
print(max(dp[-1]))