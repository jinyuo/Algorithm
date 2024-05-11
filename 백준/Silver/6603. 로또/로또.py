from itertools import combinations
import sys

while True:
    k, *S = map(int, sys.stdin.readline().split())
    if k == 0:
        break
    for comb in combinations(S, 6):
        print(*comb)
    print()