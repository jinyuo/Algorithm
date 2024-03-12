import sys
n = int(sys.stdin.readline())
d = dict()
for _ in range(n):
    k = int(sys.stdin.readline())
    if k in d.keys():
        d[k] += 1
    else:
        d[k] = 1
m = max(d.values())
key = [k for k, v in d.items() if v == m]
print(min(key))