import sys
for i in sys.stdin:
    if i == "\n":
        exit()
    h, p = map(int, i.split())
    print("{0:.2f}".format(h/p))