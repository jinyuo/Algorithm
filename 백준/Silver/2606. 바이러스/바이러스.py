import sys


def make_graph(cnt_pair: int) -> dict:
    graph = {}
    for _ in range(cnt_pair):
        pair = list(map(int, sys.stdin.readline().split()))
        len_pair = len(pair)
        for i in range(len_pair):
            if pair[i] in graph:
                graph[pair[i]].append(pair[len_pair - 1 - i])
            else:
                graph[pair[i]] = [pair[len_pair - 1 - i]]
    return graph


def bfs(graph: dict, start: int = 1) -> dict:
    visited = {k: False for k in graph.keys()}

    if not start in graph.keys():
        return visited

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
graph = make_graph(cnt_pair)
infection = bfs(graph)
print(len([k for k, v in infection.items() if k != start and v]))