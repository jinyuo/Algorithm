import sys
n = int(sys.stdin.readline())
for i in range(0, n):
    print(" " * i, "*" * (2 * n - 2 * i - 1), sep="")
for i in range(n - 1, 0, -1):
    print(" " * (i - 1), "*" * (2 * n - 2 * i + 1), sep="")