import sys

def make_graph(cnt_computor: int, cnt_pair: int) -> dict:
    graph = {k: [] for k in range(1, cnt_computor + 1)}
    for _ in range(cnt_pair):
        a, b = map(int, sys.stdin.readline().split())
        graph[a].append(b)
        graph[b].append(a)
    return graph


def bfs(graph: dict, start: int = 1) -> dict:
    visited = {k: False for k in graph.keys()}
    queue = [start]
    visited[start] = True
    while queue:
        curr = queue.pop(0)
        for i in graph[curr]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
    return visited

cnt_computor = int(sys.stdin.readline())
cnt_pair = int(sys.stdin.readline())
start = 1
graph = make_graph(cnt_computor, cnt_pair)
infection = bfs(graph)
print(len([k for k, v in infection.items() if k != start and v]))