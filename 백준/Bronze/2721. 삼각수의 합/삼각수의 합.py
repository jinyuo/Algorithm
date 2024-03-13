import sys

T = int(sys.stdin.readline())
for _ in range(T):
    n = int(sys.stdin.readline())
    print(sum([i * (i + 1) * (i + 2) // 2 for i in range(n + 1)]))