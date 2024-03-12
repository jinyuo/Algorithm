import sys
li = ['c=', 'c-', 'd-', 'lj', 'nj', 's=', 'z=']
inp = sys.stdin.readline()[:-1]
c = 0
i = 0
while i < len(inp):
    if inp[i:i + 3] == 'dz=':
        c += 1
        i += 3
    elif inp[i:i + 2] in li:
        c += 1
        i += 2
    else:
        c += 1
        i += 1
print(c)
