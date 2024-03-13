import sys
t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    store = sorted(list(map(int, sys.stdin.readline().split())))
    s = 0
    for i in range(1, n):
        s += store[i] - store[i - 1]
    print(s * 2)
