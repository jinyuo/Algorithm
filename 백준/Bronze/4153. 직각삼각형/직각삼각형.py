import sys
while True:
    l = sorted(list(map(int, sys.stdin.readline().split())))
    if l[0] == 0 and l[1] == 0 and l[2] == 0:
        exit()
    print("right" if l[0] ** 2 + l[1] ** 2 == l[2] ** 2 else "wrong")