import sys
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


for _ in '_' * int(sys.stdin.readline()):
    a, b = map(int, sys.stdin.readline().split())
    g = gcd(a, b)
    print(a * b // g, g)