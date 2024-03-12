import sys
li = ['i', 'pa', 'te', 'ni', 'niti', 'a', 'ali', 'nego', 'no', 'ili']
inp = sys.stdin.readline().split()
print(*[inp[i][0].upper() for i in range(len(inp)) if i == 0 and inp[i] in li or inp[i] not in li], sep="")