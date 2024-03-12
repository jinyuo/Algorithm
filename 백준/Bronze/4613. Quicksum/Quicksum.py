import sys
v = " ABCDEFGHIJKLMNOPQRSTUVWXYZ"
while True:
    inp = sys.stdin.readline()[:-1]
    if inp == "#":
        exit()
    checksum = 0
    for i in range(len(inp)):
        checksum += (i + 1) * v.index(inp[i])
    print(checksum)