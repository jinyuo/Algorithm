import sys
k = int(sys.stdin.readline())
for _ in range(k):
    p, m = map(int, sys.stdin.readline().split())
    s = set([int(sys.stdin.readline()) for _ in range(p)])
    print(p - len(s))