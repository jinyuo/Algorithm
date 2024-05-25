import sys

case = int(sys.stdin.readline())
for _ in range(case):
    N, M = map(int, sys.stdin.readline().split())
    queue = list(enumerate(map(int, sys.stdin.readline().split())))

    answer = 1
    while queue:
        v = queue.pop(0)
        if queue and v[1] < max(q[1] for q in queue):
            queue.append(v)
        else:
            if M == v[0]:
                break
            else:
                answer += 1
    print(answer)
