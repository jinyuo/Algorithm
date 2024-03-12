import sys
s, e = map(int, sys.stdin.readline().split())
ss = []
i = 1
while len(ss) <= 1000:
    for _ in range(i):
        ss.append(i)
    i += 1
print(sum(ss[s - 1:e]))