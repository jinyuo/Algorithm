import sys
t = int(sys.stdin.readline())
for i in range(t):
    ys = ks = 0
    for j in range(9):
        y, k = map(int, sys.stdin.readline().split())
        ys += y
        ks += k
    print("Yonsei" if ys > ks else ("Korea" if ys < ks else "Draw"))