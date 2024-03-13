import sys
search = sys.stdin.readline()[:-1]
n = int(sys.stdin.readline())
c = 0
for _ in range(n):
    i = sys.stdin.readline()[:-1]
    i += i[:len(search)-1]
    if i.find(search) >= 0:
        c += 1
print(c)