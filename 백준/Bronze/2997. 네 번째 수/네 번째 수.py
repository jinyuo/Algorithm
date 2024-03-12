import sys
li = sorted(list(map(int, sys.stdin.readline().split())))
g = [li[1] - li[0], li[2] - li[1]]
print(li[2] + g[1] if g[0] == g[1] else li[1] + g[0] if g[0] < g[1] else li[1] - g[1])