import sys
a = 5 * 60
b = 60
c = 10
t = int(sys.stdin.readline())

if t % c != 0:
    print(-1)
else:
    ar = t // a
    t %= a
    br = t // b
    t %= b
    print(ar, br, t // c)