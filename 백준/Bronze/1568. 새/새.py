import sys
n = int(sys.stdin.readline())
c = 0
i = 1
while n > 0:
    if i > n:
        i = 1
    c += 1
    n -= i
    i += 1
print(c)