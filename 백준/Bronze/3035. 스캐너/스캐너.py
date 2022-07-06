import sys
r, c, zr, zc = map(int, sys.stdin.readline().split())
news = [sys.stdin.readline()[:-1] for _ in range(r)]
for n in news:
    for _ in range(zr):
        print("".join([n[i] * zc for i in range(c)]))
