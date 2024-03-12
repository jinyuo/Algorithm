import sys
t = m = 0
for i in range(4):
    o, i = map(int, sys.stdin.readline().split())
    t += - o + i
    if t > m:
        m = t
print(m)