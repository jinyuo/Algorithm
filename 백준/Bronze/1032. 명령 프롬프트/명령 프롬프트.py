import sys
n = int(sys.stdin.readline())
r = ""
for i in range(n):
    if i == 0:
        r = sys.stdin.readline()[:-1]
    else:
        tmp = sys.stdin.readline()[:-1]
        for j in range(len(tmp)):
            if tmp[j] != r[j] and r[j] != "?":
                r = r[:j] + "?" + r[j+1:]

print(r)