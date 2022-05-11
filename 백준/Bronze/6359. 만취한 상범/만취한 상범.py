import sys
t = int(sys.stdin.readline())

for _ in range(t):
    n = int(sys.stdin.readline())
    c = [True for _ in range(n + 1)]
    for i in range(2, n+1):
        for j in range(0, n + 1, i):
            c[j] = not c[j]
    print(c[1:].count(True))