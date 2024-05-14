import sys


def bfs(maps, n, m, start=(0, 0)):
    visited = [[False for _ in range(m)] for _ in range(n)]
    directions = [(1, 0), (0, -1), (-1, 0), (0, 1)]
    queue = [start]
    visited[start[0]][start[1]] = True

    while queue:
        i, j = queue.pop(0)
        for x, y in directions:
            ni, ny = i + x, j + y
            if 0 <= ni < n and 0 <= ny < m and maps[ni][ny] == 1:
                if visited[ni][ny] == 0:
                    queue.append((ni, ny))
                    visited[ni][ny] = True
    return visited


n = int(sys.stdin.readline())
maps = [list(map(int, sys.stdin.readline().strip())) for _ in range(n)]

visited = [[False for _ in range(n)] for _ in range(n)]
list_cnt = []
for i in range(n):
    for j in range(n):
        if maps[i][j] == 1 and not visited[i][j]:
            temp = bfs(maps, n, n, start=(i, j))
            visited = [[temp[x][y] | visited[x][y] for y in range(n)] for x in range(n)]
            list_cnt.append(len([i for i in sum(temp, []) if i]))

list_cnt.sort()
print(len(list_cnt))
print("\n".join(str(n) for n in list_cnt))