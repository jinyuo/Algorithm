import sys
t = int(sys.stdin.readline())
for _ in range(t):
    n, d = map(int, sys.stdin.readline().split())
    co = 0
    for _ in range(n):
        v, f, c = map(int, sys.stdin.readline().split())
        if d <= v * f // c:
            co += 1
    print(co)