import sys
s = sys.stdin.read()
s = s.replace("\n", "").replace(" ", "")
d = dict()
for t in sorted(set(s)):
    d[t] = s.count(t)
for k, v in d.items():
    if v == max(d.values()):
        print(k, end="")