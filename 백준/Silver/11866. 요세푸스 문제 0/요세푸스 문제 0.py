from collections import deque
import sys

n, k = map(int, sys.stdin.readline().split())
li = deque([i + 1 for i in range(n)])
order = []
while li:
    for i in range(k - 1):
        li.append(li.popleft())
    order.append(li.popleft())
print('<' + ', '.join(str(o) for o in order)+'>')