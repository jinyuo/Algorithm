def solution(maps):
    n = len(maps[0])
    m = len(maps)
    visited = [[0 for _ in range(n)] for _ in range(m)]
    queue = [(0, 0)]
    visited[0][0] = 1
    nxt_gap = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    while queue:
        i, j = queue.pop(0)
        
        for x, y in nxt_gap:
            nx, my = i + x, j + y
            
            if 0 <= nx < m and 0 <= my < n and maps[nx][my] == 1 and visited[nx][my] == 0:
                queue.append((nx, my))
                visited[nx][my] = visited[i][j] + 1

            
    if visited[-1][-1] == 0:
        return -1
    return visited[-1][-1]