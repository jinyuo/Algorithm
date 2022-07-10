import sys
n, m = map(int, sys.stdin.readline().split())
mosaic = [[0 for _ in range(100)] for _ in range(100)]
for _ in range(n):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    for x in range(x1 - 1, x2):
        for y in range(y1 - 1, y2):
            mosaic[x][y] += 1
print(len([mosaic[i][j] for i in range(100) for j in range(100) if mosaic[i][j] > m]))