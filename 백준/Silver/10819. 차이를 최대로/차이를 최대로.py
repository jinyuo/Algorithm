import sys
n = int(sys.stdin.readline())
nums = sorted(list(map(int, sys.stdin.readline().split())))
sort_nums = []
c = True
while nums:
    if len(nums) == 1:
        sort_nums.insert(0 if abs(sort_nums[0] - nums[0]) > abs(sort_nums[-1] - nums[0]) else n - 1, nums[0])
        break
    sort_nums.insert(0, nums.pop() if c else nums.pop(0))
    sort_nums.append(nums.pop(0) if c else nums.pop())
    c = not c
    
print(sum([abs(sort_nums[i] - sort_nums[i + 1]) for i in range(n - 1)]))