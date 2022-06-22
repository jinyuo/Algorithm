import sys
import math
n = int(sys.stdin.readline())
li = list(map(int, sys.stdin.readline().split()))
for i in range(1, n):
    g = math.lcm(li[0], li[i])
    print(f"{g // li[i]}/{g // li[0]}")