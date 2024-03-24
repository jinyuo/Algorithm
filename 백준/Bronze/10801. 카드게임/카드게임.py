import sys
c = [list(map(int, sys.stdin.readline().split())) for _ in range(2)]
w = [0] * 2
for i in range(10):
    if c[0][i] != c[1][i]:
        w[0 if c[0][i] > c[1][i] else 1] += 1
print("D" if w[0] == w[1] else "A" if w[0] > w[1] else "B")