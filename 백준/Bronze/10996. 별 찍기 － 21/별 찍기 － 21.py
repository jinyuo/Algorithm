import sys

n = int(sys.stdin.readline())

first = ['*' if i % 2 == 0 else ' ' for i in range(n)]
second = [' ' if i % 2 == 0 else '*' for i in range(n)]

for i in range(2 * n):
    print(''.join(first if i % 2 == 0 else second))