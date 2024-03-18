import sys
n = int(sys.stdin.readline())
c = s = 100
for i in range(n):
    ct, st = map(int, sys.stdin.readline().split())
    if ct > st:
        s -= ct
    elif ct < st:
        c -= st
print(c, s, sep="\n")