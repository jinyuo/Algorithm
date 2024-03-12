import sys
t = m = 0
for _ in range(10):
    o, i = map(int, sys.stdin.readline().split())
    t += i - o
    if t > m:
        m = t
print(m)