import sys
b = [1, 1, 2, 2, 2, 8]
w = list(map(int, sys.stdin.readline().split()))

print(" ".join([str(b[i] - w[i]) for i in range(len(b))]))