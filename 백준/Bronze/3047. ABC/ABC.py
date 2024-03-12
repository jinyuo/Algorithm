import sys
abcs = sorted(list(map(int, sys.stdin.readline().split())))
d = dict()
for i in range(3):
    d[chr(ord("A") + i)] = abcs[i]
p = sys.stdin.readline()[:-1]
for i in p:
    print(d[i], end=" ")