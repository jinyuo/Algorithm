import sys
n, w, h = map(int, sys.stdin.readline().split())
for _ in range(n):
    l = int(sys.stdin.readline())
    print("DA" if w ** 2 + h ** 2 >= l ** 2 else "NE")