import sys
n = int(sys.stdin.readline())
print((5 if n == 1 else (3 * n ** 2 + 5 * n + 2) // 2) % 45678)