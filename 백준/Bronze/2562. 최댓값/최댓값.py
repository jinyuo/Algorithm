import sys
l = []
for i in range(9):
    l.append(int(sys.stdin.readline()))
m = max(l)
print(m, l.index(m) + 1, sep="\n")