import sys
m = int(sys.stdin.readline())
n = int(sys.stdin.readline())
r = int(m ** 0.5)
s = []
while r ** 2 <= n:
    t = r ** 2
    if t >= m:
        s.append(t)
    r += 1
    
if len(s) > 0:
    print(sum(s), min(s), sep="\n")
else:
    print(-1)