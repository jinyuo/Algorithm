import sys

a, b = map(int, sys.stdin.readline().split())
SIZE = 4
ax, ay = divmod(a - 1, SIZE)
bx, by = divmod(b - 1, SIZE)
print(abs(ax - bx) + abs(ay - by))