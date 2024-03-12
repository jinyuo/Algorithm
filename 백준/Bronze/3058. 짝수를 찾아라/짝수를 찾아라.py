import sys
t = int(sys.stdin.readline())
for _ in range(t):
    nums = [i for i in map(int, sys.stdin.readline().split()) if i % 2 == 0]
    print(sum(nums), min(nums))