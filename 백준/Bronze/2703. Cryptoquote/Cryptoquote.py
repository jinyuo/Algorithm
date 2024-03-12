import sys
t = int(sys.stdin.readline())
fr = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
for _ in range(t):
    plain = sys.stdin.readline()[:-1]
    to = sys.stdin.readline()[:-1]
    print(plain.translate(plain.maketrans(fr, to)))