import sys
while True:
    s = sys.stdin.readline()
    if s == "EOI\n":
        exit()
    print("Found" if s.upper().find("NEMO") > -1 else "Missing")