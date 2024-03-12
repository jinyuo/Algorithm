from itertools import permutations
import sys
n = int(sys.stdin.readline())
for t in permutations([i for i in range(1, n + 1)], n):
    print(*t)