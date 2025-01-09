import sys

n = int(sys.stdin.readline())
q, r = divmod(n, 2)
print((1 + q) * (1 + q + r))