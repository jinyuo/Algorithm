import sys
n = int(sys.stdin.readline())
for _ in range(n):
    t = sys.stdin.readline()[:-1]
    print("skipped" if t == "P=NP" else eval(t))