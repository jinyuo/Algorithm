import sys

def bfs(graph, n, m, visited, cnt=0, start=(0, 0)):
    if graph[start[0]][start[1]] == 0 or visited[start[0]][start[1]] != 0:
        return visited, cnt

    queue = [start]
    directions = [(1, 0), (0, -1), (-1, 0), (0, 1)]
    cnt += 1
    size = 1
    visited[start[0]][start[1]] = size

    while queue:
        i, j = queue.pop(0)

        for x, y in directions:
            ni, ny = i + x, j + y

            if 0 <= ni < n and 0 <= ny < m and graph[ni][ny] == 1:
                if visited[ni][ny] == 0:
                    queue.append((ni, ny))
                    size += 1
                    visited[ni][ny] = size

    return visited, cnt

n, m = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().split())) for i in range(n)]
visited = [[0 for _ in range(m)] for _ in range(n)]
cnt = 0
for i in range(n):
    for j in range(m):
        visited, cnt = bfs(graph, n, m, visited, cnt, start=(i, j))

print(cnt)
print(max(sum(visited, [])))