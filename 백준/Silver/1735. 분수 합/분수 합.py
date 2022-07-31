import sys, math
a1, b1 = map(int, sys.stdin.readline().split())
a2, b2 = map(int, sys.stdin.readline().split())
b = math.lcm(b1, b2)
a = a1 * (b // b1) + a2 * (b // b2)
r = math.gcd(a, b)
print(a // r, b // r)