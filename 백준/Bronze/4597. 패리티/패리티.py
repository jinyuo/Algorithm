import sys
while True:
    s = sys.stdin.readline()[:-1]
    if s == "#":
        exit()
    if s[-1] == "e":
        print(s.replace("e", "1") if s.count("1") % 2 == 1 else s.replace("e", "0"))
    else:
        print(s.replace("o", "1") if s.count("1") % 2 == 0 else s.replace("o", "0"))