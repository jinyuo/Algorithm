import sys
import collections
n = int(sys.stdin.readline())
card = collections.deque([i for i in range(1, n + 1)])
while len(card) > 1:
    card.popleft()
    card.append(card.popleft())
print(card.pop())