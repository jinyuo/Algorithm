import sys
loop = int(sys.stdin.readline())
for _ in range(loop):
    s = int(sys.stdin.readline())
    n = int(sys.stdin.readline())
    for _ in range(n):
        q, p = map(int, sys.stdin.readline().split())
        s += q * p
    print(s)