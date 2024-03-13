import sys
t = int(sys.stdin.readline())
c = [350.34, 230.90, 190.55, 125.30, 180.90]
for _ in range(t):
    l = list(map(int, sys.stdin.readline().split()))
    print("${0:.2f}".format(sum([c[i]*l[i] for i in range(len(c))])))