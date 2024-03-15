import sys
t = int(sys.stdin.readline())
for _ in range(t):
    li = sys.stdin.readline().split()
    print(" ".join(l[::-1] for l in li))