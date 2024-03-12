import sys
a = list(map(int, sys.stdin.readline().split()))
b = list(map(int, sys.stdin.readline().split()))
w = []
for i in range(len(a)):
    w.append("D" if a[i] == b[i] else ("A" if a[i] > b[i] else "B"))
a_s, b_s = 3 * w.count("A") + w.count("D"), 3 * w.count("B") + w.count("D")
print(a_s, b_s)
if a_s == b_s:
    for t in w[::-1]:
        if t != "D":
            print(t)
            exit()
    print("D")
else:
    print("A" if a_s > b_s else "B")
