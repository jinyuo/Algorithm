import sys
n = int(sys.stdin.readline())
e = dict()
for _ in range(n):
    n, f = sys.stdin.readline().split()
    if f == "enter":
        e[n] = True
    else:
        del e[n]
print("\n".join(i for i in sorted(e.keys(), reverse=True)))