import sys
n = int(sys.stdin.readline())
l = sorted(list(map(int, sys.stdin.readline().split())))
print(l[0] * l[-1])