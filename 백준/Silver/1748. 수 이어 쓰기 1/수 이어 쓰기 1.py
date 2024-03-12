import sys
n = int(sys.stdin.readline())
c = 0
i = 1
while i <= n:
    c += n - i + 1
    i *= 10
print(c)