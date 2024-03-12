import sys
t = int(sys.stdin.readline())
for _ in range(t):
    i, s = sys.stdin.readline().split()
    s = list(s)
    s.pop(int(i) - 1)
    print("".join(s))