import sys

w_board = ['WB' * 4 if i % 2 == 0 else 'BW' * 4 for i in range(8)]
b_board = ['BW' * 4 if i % 2 == 0 else 'WB' * 4 for i in range(8)]


def check_board(board, i, j, mode='W'):
    cnt = 0
    using_board = w_board if mode == 'W' else b_board
    for x in range(8):
        for y in range(8):
            if using_board[x][y] != board[i + x][j + y]:
                cnt += 1
    return cnt


N, M = map(int, sys.stdin.readline().split())
board = [sys.stdin.readline().strip() for _ in range(N)]
result = [check_board(board, i, j, mode='W') for i in range(N - 7) for j in range(M - 7)]
result.extend([check_board(board, i, j, mode='B') for i in range(N - 7) for j in range(M - 7)])
print(min(result))