import sys
def gcd(a, b):
    if a % b == 0:
        return b
    return gcd(b, a % b)

            
a, b = map(int, sys.stdin.readline().split())
g = gcd(a, b)
print(g, a * b // g, sep="\n")
