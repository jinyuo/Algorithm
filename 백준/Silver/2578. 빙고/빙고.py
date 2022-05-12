import sys
board = [list(map(int, sys.stdin.readline().split())) for _ in range(5)]
lo = list()
for _ in range(5):
    call = list(map(int, sys.stdin.readline().split()))
    for c in call:
        lo.append([[i, j] for i in range(5) for j in range(5) if board[i][j] == c][0])

        b = 0
        for x in range(5):
            if [l[0] for l in lo].count(x) == 5:
                b += 1
            if [l[1] for l in lo].count(x) == 5:
                b += 1
        if len([l for l in lo if l[0] == l[1]]) == 5:
            b += 1
        if len([l for l in lo if l[0] + l[1] == 4]) == 5:
            b += 1
        if b >= 3:
            print(len(lo))
            exit()