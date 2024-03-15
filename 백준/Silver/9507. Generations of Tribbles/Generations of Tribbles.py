import sys
p = [1, 1, 2, 4]
t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    if len(p) <= n:
        for i in range(len(p), n + 1):
            p.append(p[i - 1] + p[i - 2] + p[i - 3] + p[i - 4])
    print(p[n])