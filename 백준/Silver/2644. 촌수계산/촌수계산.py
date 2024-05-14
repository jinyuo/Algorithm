import sys


def make_graph(n, m):
    graph = {i: [] for i in range(1, n + 1)}
    for _ in range(m):
        x, y = map(int, sys.stdin.readline().split())
        graph[x].append(y)
        graph[y].append(x)
    return graph


def bfs(graph, start):
    visited = {k: -1 for k in graph.keys()}
    queue = [start]
    visited[start] = 0

    while queue:
        curr = queue.pop(0)

        for node in graph[curr]:
            if visited[node] == -1:
                queue.append(node)
                visited[node] = visited[curr] + 1
    return visited


n = int(sys.stdin.readline())
start, end = map(int, sys.stdin.readline().split())
m = int(sys.stdin.readline())
graph = make_graph(n, m)
relatives = bfs(graph, start=start)
print(relatives[end])