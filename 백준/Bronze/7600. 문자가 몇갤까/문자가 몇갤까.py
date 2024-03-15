import sys
while True:
    inp = sys.stdin.readline()[:-1].upper()
    if inp == "#":
        exit()

    inp = set(filter(str.isalpha, inp))
    print(len(set(inp)))