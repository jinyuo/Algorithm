import sys
def gcd(a, b):
    if a % b == 0:
        return b
    else:
        return gcd(b, a % b)


n = int(sys.stdin.readline())
if n == 2:
    a, b = map(int, sys.stdin.readline().split())
    gcd_val = gcd(a, b)
else:
    a, b, c = map(int, sys.stdin.readline().split())
    gcd_val = gcd(gcd(a, b), c)

f = []
d = 1
while d <= gcd_val ** 0.5:
    if gcd_val % d == 0:
        f.append(d)
        f.append(gcd_val // d)
    d += 1
f = list(set(f))
f.sort()
print("\n".join(str(i) for i in f))
