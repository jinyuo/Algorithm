import sys
m = int(sys.stdin.readline())
cup = {1: 1, 2: 2, 3: 3} # cup_num: location
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    cup[a], cup[b] = cup[b], cup[a]
print([k for k, v in cup.items() if v == 1][0])