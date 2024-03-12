import sys
w = sys.stdin.readline()[:-1]
for i in "CAMBRIDGE":
    w = w.replace(i, "")
print(w)