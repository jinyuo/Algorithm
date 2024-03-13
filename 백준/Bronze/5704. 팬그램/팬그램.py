import sys
for i in sys.stdin:
    if i == "*\n":
        exit()
    print("N" if len(set("".join(i[:-1].split()))) < 26 else "Y")