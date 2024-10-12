import sys

R, C = map(int, sys.stdin.readline().split())
A, B = map(int, sys.stdin.readline().split())
BLACK = 'X'
WHITE = '.'

for i in range(R * A):
    if i // A % 2 == 0:
        start, residue = BLACK, WHITE
    else:
        start, residue = WHITE, BLACK
    print("".join((start if j % 2 == 0 else residue) * B for j in range(0, C)))