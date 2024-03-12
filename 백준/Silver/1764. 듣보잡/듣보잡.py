import sys
n, m = map(int, sys.stdin.readline().split())
c = []
l = set()
for _ in range(n+m):
    t = sys.stdin.readline()[:-1]
    if t in l:
        c.append(t)
    l.add(t)
print(len(c))
print("\n".join(sorted(c)))