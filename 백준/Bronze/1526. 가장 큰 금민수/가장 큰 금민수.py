import sys
n = int(sys.stdin.readline())
for i in range(n, 3, -1):
    s = set(str(i))
    f = True
    for t in s:
        if t in set("01235689"):
            f = False
    if f:
        print(i)
        exit()