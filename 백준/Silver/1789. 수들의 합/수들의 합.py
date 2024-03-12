import sys

n = int(sys.stdin.readline())
i = 2

if n in {1, 2}:
    print(1)
else:
    while i * (i - 1) // 2 <= n:
        i += 1
    print(i - 2)