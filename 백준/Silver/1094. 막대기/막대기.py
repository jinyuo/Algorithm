import sys
s = [64]
x = int(sys.stdin.readline())
while sum(s) > x:
    t = s.pop() // 2
    if sum(s) + t < x:
        s.append(t)

    s.append(t)
print(len(s))