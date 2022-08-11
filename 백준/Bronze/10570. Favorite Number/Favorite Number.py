import sys
n = int(sys.stdin.readline())
for _ in range(n):
    d = dict()
    v = int(sys.stdin.readline())
    for _ in range(v):
        s = int(sys.stdin.readline())
        if s not in d.keys():
            d[s] = 1
        else:
            d[s] += 1
    print(min([ke for ke, val in d.items() if val == max(d.values())]))