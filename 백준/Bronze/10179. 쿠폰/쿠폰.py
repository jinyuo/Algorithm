import sys
n = int(sys.stdin.readline())
for _ in range(n):
    print("${0:.2f}".format(round(float(sys.stdin.readline()) * 0.8, 2)))