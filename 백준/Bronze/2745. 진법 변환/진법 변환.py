import sys
notation = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
n, b = sys.stdin.readline().split()
b = int(b)
s = notation.index(n[len(n) - 1])

for i in range(len(n) - 2, -1, -1):
    s += notation.index(n[i]) * b ** (len(n) - 1 - i)
print(s)