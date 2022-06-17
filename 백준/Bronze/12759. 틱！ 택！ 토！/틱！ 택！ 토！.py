import sys
f = int(sys.stdin.readline())
p = [[10 * (i + 1) + j for i in range(3)] for j in range(3)]
for _ in range(9):
    x, y = map(int, sys.stdin.readline().split())
    if f == 1:
        p[x - 1][y - 1] = 1
        f = 2
    elif f == 2:
        p[x - 1][y - 1] = 2
        f = 1
    for i in range(3):
        if p[i][0] == p[i][1] == p[i][2]:
            print(p[i][1])
            exit()
        elif p[0][i] == p[1][i] == p[2][i]:
            print(p[1][i])
            exit()
        elif p[0][0] == p[1][1] == p[2][2] or p[0][2] == p[1][1] == p[2][0]:
            print(p[1][1])
            exit()
print(0)