import sys
while True:
    a = list(map(int, sys.stdin.readline().split()))
    if a[0] == 0 and a[1] == 0 and a[2] == 0:
        exit()
    if a[1] - a[0] == a[2] - a[1]:
        print(f"AP {a[2] + a[1] - a[0]}")
    else:
        print(f"GP {a[2] * (a[2] // a[1])}")