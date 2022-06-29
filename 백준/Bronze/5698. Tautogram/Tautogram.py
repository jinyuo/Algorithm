import sys
while True:
    case = sys.stdin.readline()[:-1]
    if case == '*':
        exit()
    s = set(c[0].upper() for c in case.split())
    print("Y" if len(s) == 1 else "N")