import sys
n, k = map(int, sys.stdin.readline().split())
c = r = 0
for i in range(1, n + 1):
    if n % i == 0:
        c += 1
    if c == k and r == 0:
        r = i
print(r)
