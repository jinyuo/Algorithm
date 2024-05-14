import sys

def make_graph(cnt_computor: int, cnt_pair: int) -> dict:
    graph = {k: [] for k in range(1, cnt_computor + 1)}
    for _ in range(cnt_pair):
        a, b = map(int, sys.stdin.readline().split())
        graph[a].append(b)
        graph[b].append(a)
    return graph

def dfs(graph: dict, start: int = 1) -> dict:
    visited = []
    need_visit = [start]

    while need_visit:
        curr = need_visit.pop()
        if curr not in visited:
            visited.append(curr)
            need_visit.extend(graph[curr])
    return visited

cnt_computor = int(sys.stdin.readline())
cnt_pair = int(sys.stdin.readline())
start = 1
graph = make_graph(cnt_computor, cnt_pair)
infection = dfs(graph, start)
print(len([i for i in infection if i != start]))