import sys
n, m = map(int, sys.stdin.readline().split())
p = [sorted(map(int, sys.stdin.readline().split()), reverse=True) for _ in range(n)]
s = [0 for _ in range(n)]
for i in range(m):
    r = [t[i] for t in p]
    for j in range(n):
        if max(r) == r[j]:
            s[j] += 1

print(" ".join([str(i + 1) for i in range(n) if s[i] == max(s)]))