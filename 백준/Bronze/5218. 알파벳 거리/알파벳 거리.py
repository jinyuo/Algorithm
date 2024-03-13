import sys
n = int(sys.stdin.readline())
for _ in range(n):
    a, b = sys.stdin.readline().split()
    r = []
    for i in range(len(a)):
        d = ord(b[i]) - ord(a[i])
        if d >= 0:
            r.append(d)
        else:
            r.append(d + 26)
    print(f"Distances: " + " ".join(str(i) for i in r))