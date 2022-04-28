import sys
n = int(sys.stdin.readline())
code = [sys.stdin.readline()[:-1] for _ in range(n)]
code = sorted(code, key=lambda x: (len(x), sum([int(i) for i in x if i.isnumeric()]), x))
print("\n".join(code))