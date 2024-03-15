import sys
n = int(sys.stdin.readline())
xy_list = []
r = []
for _ in range(n):
    x, y = map(int, sys.stdin.readline().split())
    xy_list.append((x, y))
for x, y in xy_list:
    rank = 1
    for p, q in xy_list:
        rank += 1 if x < p and y < q else 0
    r.append(str(rank))
print(" ".join(rank for rank in r))