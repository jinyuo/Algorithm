import sys
n = int(sys.stdin.readline())
l = set(sys.stdin.readline()[:-1] for _ in range(n))
l = sorted(list(l))
l = sorted(l, key=len)
print("\n".join(x for x in l))