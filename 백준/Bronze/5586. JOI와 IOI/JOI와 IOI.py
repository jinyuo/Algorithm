import sys
inp = sys.stdin.readline()[:-1]
joi = 0
ioi = 0
for i in range(len(inp)):
    if inp[i:i+3] == "JOI":
        joi += 1
    elif inp[i:i+3] == "IOI":
        ioi += 1
print(joi, ioi, sep="\n")