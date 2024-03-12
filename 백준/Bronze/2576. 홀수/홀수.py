import sys
l = []
for _ in range(7):
    n = int(sys.stdin.readline())
    if n % 2:
        l.append(n)
if len(l):
    print(sum(l), min(l), sep="\n")
else:
    print(-1)