import sys
n = int(sys.stdin.readline()[:-3] + "00")
f = int(sys.stdin.readline())
for i in range(n, n + 99):
    if i % f == 0:
        print(str(i)[-2:])
        break