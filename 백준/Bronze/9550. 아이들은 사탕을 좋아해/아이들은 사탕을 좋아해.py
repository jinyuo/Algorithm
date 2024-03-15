import sys
t = int(sys.stdin.readline())
for _ in range(t):
    n, k = map(int, sys.stdin.readline().split())
    li = map(int, sys.stdin.readline().split())
    c = 0
    for l in li:
        c += l // k
    print(c)