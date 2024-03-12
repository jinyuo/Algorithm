import sys
l = sys.stdin.readline()
s = ""
for i in l:
    if i.isupper():
        s += i
print(s)