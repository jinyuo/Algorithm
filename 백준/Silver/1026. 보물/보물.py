import sys
n = int(sys.stdin.readline())
a = sorted(list(map(int, sys.stdin.readline().split())))
b = sorted(list(map(int, sys.stdin.readline().split())), reverse=True)

print(sum(a[i] * b[i] for i in range(n)))