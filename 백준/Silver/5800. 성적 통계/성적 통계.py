import sys
k = int(sys.stdin.readline())
for i in range(1, k + 1):
    score = list(map(int, sys.stdin.readline().split()))
    n = score.pop(0)
    score = sorted(score)
    gap = 0
    for j in range(n - 1):
        g = score[j + 1] - score[j]
        if g > gap:
            gap = g
    print(f"Class {i}")
    print(f"Max {max(score)}, Min {min(score)}, Largest gap {gap}")