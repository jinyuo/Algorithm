import sys
maxs, num = 0, -1
for i in range(5):
    score = sum(list(map(int, sys.stdin.readline().split())))
    if maxs < score:
        maxs, num = score, i
print(num + 1, maxs)