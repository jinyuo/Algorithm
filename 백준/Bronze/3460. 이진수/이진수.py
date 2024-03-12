import sys
t = int(sys.stdin.readline())
for _ in range(t):
    n = "{0:b}".format(int(sys.stdin.readline()))[::-1]
    print(" ".join([str(i) for i in range(len(n)) if n[i] == "1"]))