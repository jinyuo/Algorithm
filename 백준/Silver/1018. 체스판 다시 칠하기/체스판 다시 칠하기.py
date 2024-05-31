import sys

size = 8
w_board = ['WB' * (size // 2) if i % 2 == 0 else 'BW' * (size // 2) for i in range(size)]
b_board = ['BW' * (size // 2) if i % 2 == 0 else 'WB' * (size // 2) for i in range(size)]


def check_board(board, i, j, mode='W'):
    cnt = 0
    using_board = w_board if mode == 'W' else b_board
    for x in range(size):
        for y in range(size):
            if using_board[x][y] != board[i + x][j + y]:
                cnt += 1
    return cnt


N, M = map(int, sys.stdin.readline().split())
board = [sys.stdin.readline().strip() for _ in range(N)]
result = [check_board(board, i, j, mode='W') for i in range(N - size + 1) for j in range(M - size + 1)]
result.extend([check_board(board, i, j, mode='B') for i in range(N - size + 1) for j in range(M - size + 1)])
print(min(result))