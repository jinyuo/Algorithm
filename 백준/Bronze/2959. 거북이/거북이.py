import sys

v = list(map(int, sys.stdin.readline().split()))
v.sort()
print(min(v[:2]) * min(v[2:]))