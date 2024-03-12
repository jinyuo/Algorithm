import sys
n = int(sys.stdin.readline())
for i in range(n):
    print(" " * (n - 1 - i), "*" * (i + 1), sep="")
for i in range(n - 1, -1, -1):
    print(" " * (n - i), "*" * i, sep="")