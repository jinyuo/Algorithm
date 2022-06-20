import sys
pan = [[-1 for _ in range(1001)] for _ in range(1001)]
n = int(sys.stdin.readline())
for i in range(n):
    a, b, x, y = map(int, sys.stdin.readline().split())
    for at in range(a, a + x):
        for bt in range(b, b + y):
           pan[at][bt] = i

pan = sum(pan, [])
for i in range(n):
    print(pan.count(i))