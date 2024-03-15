import sys
t = int(sys.stdin.readline())
for _ in range(t):
    nums = sorted(list(map(int, sys.stdin.readline().split())))[1:4]
    print(sum(nums) if nums[2] - nums[0] < 4 else "KIN")