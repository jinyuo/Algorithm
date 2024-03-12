import sys
l = list(map(int, sys.stdin.readline().split()))
for i in range(len(l)-1):
    if i == 0:
        f = False
        d = "a" if l[i] < l[i+1] else "d"
    else:
        if (d == "a" and l[i] > l[i+1]) or (d == "d" and l[i] < l[i+1]):
            f = True
            break
print("mixed" if f == True else ("ascending" if d == "a" else "descending"))