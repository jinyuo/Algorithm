import sys
m = sys.stdin.readline()
s, h = m.count(":-("), m.count(":-)")
if s + h == 0:
    print("none")
else:
    if s == h:
        print("unsure")
    elif s > h:
        print("sad")
    else:
        print("happy")