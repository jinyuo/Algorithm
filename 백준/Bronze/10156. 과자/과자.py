import sys
k, n, m = map(int, sys.stdin.readline().split())
r = k * n - m
print(0 if r < 0 else r)