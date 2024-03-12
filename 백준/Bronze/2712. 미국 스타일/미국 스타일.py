import sys
t = int(sys.stdin.readline())
for _ in range(t):
    n, u = sys.stdin.readline().split()
    if u == "kg":
        print("{0:.4f}".format(float(n) * 2.2046), "lb")
    elif u == "lb":
        print("{0:.4f}".format(float(n) * 0.4536), "kg")
    elif u == "l":
        print("{0:.4f}".format(float(n) * 0.2642), "g")
    else:
        print("{0:.4f}".format(float(n) * 3.7854), "l")