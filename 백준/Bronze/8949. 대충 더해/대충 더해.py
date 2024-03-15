import sys
a, b = sys.stdin.readline().split()
if len(a) > len(b):
    b = b.zfill(len(a))
else:
    a = a.zfill(len(b))
s = ""
for i in range(len(a) - 1, -1, -1):
    s = str(int(a[i]) + int(b[i])) + s
print(s)