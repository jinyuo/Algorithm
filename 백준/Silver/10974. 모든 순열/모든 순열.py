from itertools import permutations
import sys
n = int(sys.stdin.readline())
li = [i for i in range(1, n + 1)]
for t in list(permutations(li, n)):
    print(*t)