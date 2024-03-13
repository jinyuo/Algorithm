import sys
c = 1000 - int(sys.stdin.readline())
co = [500, 100, 50, 10, 5, 1]
s = 0
for t in co:
    s += c // t
    c %= t
print(s)