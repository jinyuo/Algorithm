import sys

N, K = map(int, sys.stdin.readline().split())
max_size = 100000
visited = [-1 for _ in range(max_size + 1)]
oper = ["curr + 1", "curr - 1", "curr * 2"]
visited[N] = 0
queue = [N]

while queue:
    curr = queue.pop(0)
    if curr == K:
        break

    for o in oper:
        nxt_idx = eval(o)
        if (0 <= nxt_idx <= max_size) and visited[nxt_idx] < 0:
            visited[nxt_idx] = visited[curr] + 1
            queue.append(nxt_idx)

print(visited[K])