import sys
a, b, c = map(int, sys.stdin.readline().split())
print(max([b - a, c - b]) - 1)