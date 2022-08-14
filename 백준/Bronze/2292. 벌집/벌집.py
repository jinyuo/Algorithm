import sys
n = int(sys.stdin.readline())
l = 0
while 3 * l ** 2 + 3 * l + 1 < n:
    l += 1
print(l + 1)