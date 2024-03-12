import sys
import collections
n = int(sys.stdin.readline())
q = collections.deque()
q.append(0)
q.append(1)

if n == 0 or n == 1:
    print(n)
else:
    for i in range(2, n):
        q.append(q.popleft() + q[0])
    print(sum(q))