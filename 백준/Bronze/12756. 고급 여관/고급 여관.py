import sys
a = list(map(int, sys.stdin.readline().split()))
b = list(map(int, sys.stdin.readline().split()))
ta = (a[1] // b[0]) + (0 if a[1] % b[0] == 0 else 1)
tb = (b[1] // a[0]) + (0 if b[1] % a[0] == 0 else 1)
if ta == tb:
    print("DRAW")
elif ta > tb:
    print("PLAYER A")
else:
    print("PLAYER B")
