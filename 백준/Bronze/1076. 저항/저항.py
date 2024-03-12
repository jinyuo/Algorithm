import sys
om = ['black', "brown", 'red', "orange", "yellow", "green", "blue", "violet", "grey", "white"]
inp = [sys.stdin.readline()[:-1] for _ in range(3)]
print((om.index(inp[0]) * 10 + om.index(inp[1])) * (10 ** om.index(inp[2])))