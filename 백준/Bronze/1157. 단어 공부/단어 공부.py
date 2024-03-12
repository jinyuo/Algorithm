import sys
A = 65
s = sys.stdin.readline().upper()[:-1]
al = [0] * 26
for i in s:
    al[ord(i) - 65] += 1

m = max(al)
print(chr(al.index(m) + 65) if al.count(m) == 1 else "?")