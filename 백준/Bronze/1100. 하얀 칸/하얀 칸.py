import sys
pan = [list(sys.stdin.readline()[:-1]) for _ in range(8)]
c = 0
for i in range(8):
    for j in range(8):
        if pan[i][j] == 'F' and ((i % 2 == 0 and j % 2 == 0) or (i % 2 == 1 and j % 2 == 1)):
            c += 1
print(c)