def solution(maps):
    n = len(maps[0])
    m = len(maps)
    visited = [[0 for _ in range(n)] for _ in range(m)]
    queue = [(0, 0)]
    visited[0][0] = 1
    while queue:
        i, j = queue.pop(0)

        if i + 1 < m and maps[i + 1][j] == 1 and visited[i + 1][j] == 0:
            queue.append((i + 1, j))
            visited[i + 1][j] = visited[i][j] + 1
        if j + 1 < n and maps[i][j + 1] == 1 and visited[i][j + 1] == 0:
            queue.append((i, j + 1))
            visited[i][j + 1] = visited[i][j] + 1
        if i - 1 >= 0 and maps[i - 1][j] == 1 and visited[i - 1][j] == 0:
            queue.append((i - 1, j))
            visited[i - 1][j] = visited[i][j] + 1
        if j - 1 >= 0 and maps[i][j - 1] == 1 and visited[i][j - 1] == 0:
            queue.append((i, j - 1))
            visited[i][j - 1] = visited[i][j] + 1
            
    if visited[-1][-1] == 0:
        return -1
    return visited[-1][-1]