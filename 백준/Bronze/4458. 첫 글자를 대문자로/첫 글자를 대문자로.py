import sys
n = int(sys.stdin.readline())
for _ in range(n):
    s = sys.stdin.readline()
    print(s[0].upper() + s[1:len(s) - 1])