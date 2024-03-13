import sys
score = [sum(map(int, sys.stdin.readline().split())) for _ in range(2)]
print(max(score))