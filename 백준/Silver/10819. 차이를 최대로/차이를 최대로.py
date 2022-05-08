import sys
n = int(sys.stdin.readline())
nums = sorted(list(map(int, sys.stdin.readline().split())))
sort_nums = []
c = True
while nums:
    if len(nums) == 1:
        if abs(sort_nums[0] - nums[0]) > abs(sort_nums[-1] - nums[0]):
            sort_nums.insert(0, nums[0])
        else:
            sort_nums.append(nums[0])
        break
    min_num = nums.pop(0)
    max_num = nums.pop()

    if c:
        sort_nums.insert(0, max_num)
        sort_nums.append(min_num)
        c = False
    else:
        sort_nums.insert(0, min_num)
        sort_nums.append(max_num)
        c = True
print(sum([abs(sort_nums[i] - sort_nums[i + 1]) for i in range(n - 1)]))