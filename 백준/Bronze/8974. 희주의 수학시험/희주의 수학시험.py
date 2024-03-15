import sys
s = []
i = 1
while len(s) <= 1000:
    s += [i] * i
    i += 1
a, b = map(int, sys.stdin.readline().split())
print(sum(s[a - 1:b]))