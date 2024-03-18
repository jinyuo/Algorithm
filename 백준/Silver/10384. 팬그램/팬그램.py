import sys
alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
d = dict()
n = int(sys.stdin.readline())
for i in range(1, n + 1):
    case = sys.stdin.readline()[:-1]
    for a in alpha:
        d[a] = case.count(a) + case.count(a.lower())
    if min(d.values()) >= 3:
        print(f"Case {i}: Triple pangram!!!")
    elif min(d.values()) >= 2:
        print(f"Case {i}: Double pangram!!")
    elif min(d.values()) >= 1:
        print(f"Case {i}: Pangram!")
    else:
        print(f"Case {i}: Not a pangram")