import sys
n = int(sys.stdin.readline())
for _ in range(n):
    s = list(sys.stdin.readline()[:-1].split())
    print(" ".join(x for x in s[2:] + s[:2]))