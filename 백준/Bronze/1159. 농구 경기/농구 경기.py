import sys
n = int(sys.stdin.readline())
ln = [sys.stdin.readline()[0] for _ in range(n)]
s = [t for t in sorted(set(ln)) if ln.count(t) >= 5]
print("".join(s) if len(s) > 0 else "PREDAJA")