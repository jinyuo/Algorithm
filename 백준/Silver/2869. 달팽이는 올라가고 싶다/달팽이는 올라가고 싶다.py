import sys
a, b, v = map(int, sys.stdin.readline().split())
cnt = (v - a) // (a - b)
print(cnt + 1 if (v - a) % (a - b) == 0 else cnt + 2)