import sys
n = int(sys.stdin.readline())
board = [[0 for _ in range(100)] for _ in range(100)]

for _ in range(n):
    x, y = map(int, sys.stdin.readline().split())
    for i in range(x, x + 10):
        for j in range(y, y + 10):
            board[i][j] = 1

print(sum(board, []).count(1))