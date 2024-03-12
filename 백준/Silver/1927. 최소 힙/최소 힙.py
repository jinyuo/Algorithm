import sys
import heapq
n = int(sys.stdin.readline())
l = []
for _ in range(n):
    x = int(sys.stdin.readline())
    if x == 0:
        print(0 if not l else heapq.heappop(l))
    else:
        heapq.heappush(l, x)