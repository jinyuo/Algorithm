import sys


def dfs(maps, n, m, start=(0, 0)):
    visited = [[0 for _ in range(m)] for _ in range(n)]
    queue = [start]
    visited[start[0]][start[1]] = 1
    directions = [(1, 0), (0, -1), (-1, 0), (0, 1)]

    while queue:
        i, j = queue.pop(0)

        for x, y in directions:
            ni, ny = i + x, j + y

            if 0 <= ni < n and 0 <= ny < m and maps[ni][ny] == 1:
                if visited[ni][ny] == 0:
                    queue.append((ni, ny))
                    visited[ni][ny] = visited[i][j] + 1

    return visited


n, m = map(int, sys.stdin.readline().split())
maze = [list(map(int, list(sys.stdin.readline().strip()))) for _ in range(n)]
dfs = dfs(maze, n, m)
print(dfs[n - 1][m - 1])
