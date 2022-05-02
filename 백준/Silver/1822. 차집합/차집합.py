import sys
sys.stdin.readline()
a = set(map(int, sys.stdin.readline().split()))
b = set(map(int, sys.stdin.readline().split()))
subset = sorted(a - b)
if len(subset) == 0:
    print(0)
else:
    print(len(subset))
    print(*subset)