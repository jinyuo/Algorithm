import sys
n = int(sys.stdin.readline())
for i in range(n):
    print(" " * (n - 1 - i), "*" * (2 * i + 1), sep="")
for i in range(n - 2, -1, -1):
    print(" " * (n - 1 - i), "*" * (2 * i + 1), sep="")