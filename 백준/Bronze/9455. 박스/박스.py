import sys
t = int(sys.stdin.readline())
for _ in range(t):
    m, n = map(int, sys.stdin.readline().split())
    grid = [list((map(int, sys.stdin.readline().split()))) for _ in range(m)]
    dist = 0
    for i in range(n):
        col = [g[i] for g in grid][::-1]
        cnt = 0
        for j in range(m):
            if col[j] == 1:
                dist += j - cnt
                cnt += 1
    print(dist)