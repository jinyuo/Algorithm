import sys
n = int(sys.stdin.readline())
l = []
for i in range(n + 1):
    l.append(i if i < 2 else l[i - 2] + l[i - 1])
    
print(l[n])