import sys
t = int(sys.stdin.readline())
memo = [[0 for _ in range(101)] for __ in range(101)]
for b in range(1, 101):
    for m in range(1, 101):
        memo[b][m] = memo[b - 1][m]
        for a in range(1, b):
            if (a ** 2 + b ** 2 + m) % (a * b) == 0:
                memo[b][m] += 1

for _ in range(t):
    n, m = map(int, sys.stdin.readline().split())
    print(memo[n - 1][m])
