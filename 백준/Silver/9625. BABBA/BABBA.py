import sys
loop = int(sys.stdin.readline())
l = [(0, 1), (1, 1)]
for i in range(2, loop):
    l.append((l[i-2][0] + l[i-1][0], l[i-2][1] + l[i-1][1]))
print(*l[loop-1])