import sys
n = int(sys.stdin.readline())
for _ in range(n):
    i = sys.stdin.readline()[:-1]
    print("Yes" if i.upper() == i[::-1].upper() else "No")