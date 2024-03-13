import sys
w = [0] * 2
for _ in range(int(sys.stdin.readline())):
    a, b = map(int, sys.stdin.readline().split())
    if a > b:
        w[0] += 1
    elif a < b:
        w[1] += 1
print(" ".join(str(x) for x in w))