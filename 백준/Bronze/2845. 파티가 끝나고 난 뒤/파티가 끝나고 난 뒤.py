import sys
l, p = map(int, sys.stdin.readline().split())
t = l * p
news = list(map(int, sys.stdin.readline().split()))
print(" ".join([str(n - t) for n in news]))