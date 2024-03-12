import sys
n = int(sys.stdin.readline())
a = 0
while n >= 0:
    if n % 5 == 0:
        a += n // 5
        print(a)
        exit()
    a += 1
    n -= 3
print(-1)