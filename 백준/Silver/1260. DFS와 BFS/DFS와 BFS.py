import sys
from collections import Counter


def dfs(graph, start=1):
    visited = {k: (False, -1) for k in graph.keys()}
    stack = [start]
    i = 0

    while stack:
        cur = stack.pop()

        if not visited[cur][0]:
            i += 1
            visited[cur] = (True, i)
            stack.extend(graph[cur][::-1])

    return visited


def bfs(graph, start=1):
    visited = {k: (False, -1) for k in graph.keys()}
    queue = [start]
    i = 0
    visited[start] = (True, i)

    while queue:
        cur = queue.pop(0)

        for nxt in graph[cur]:
            if not visited[nxt][0]:
                i += 1
                queue.append(nxt)
                visited[nxt] = (True, i)
    return visited


N, M, V = map(int, sys.stdin.readline().split())
graph = {i: [] for i in range(1, N + 1)}

for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, N + 1):
    graph[i].sort()

result_dfs = sorted([(k, v[1]) for k, v in dfs(graph, start=V).items() if v[0]], key=lambda x: x[1])
result_bfs = sorted([(k, v[1]) for k, v in bfs(graph, start=V).items() if v[0]], key=lambda x: x[1])

print(*[i[0] for i in result_dfs])
print(*[i[0] for i in result_bfs])
