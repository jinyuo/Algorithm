import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
li = set()
c = 0
for i in map(int, sys.stdin.readline().split()):
    if m - i in li:
        c += 1
        li.remove(m - i)
    else:
        li.add(i)
print(c)