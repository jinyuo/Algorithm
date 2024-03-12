import sys
n = int(sys.stdin.readline())
c = list(map(int, sys.stdin.readline().split()))
s = []
for i in range(n):
    s.append(c[i] if i == 0 or c[i] == 0 else s[i - 1] + c[i])
print(sum(s))