import sys
t = int(sys.stdin.readline())
for _ in range(t):
    nums = sorted(list(map(int, sys.stdin.readline().split())))
    print(nums[7])