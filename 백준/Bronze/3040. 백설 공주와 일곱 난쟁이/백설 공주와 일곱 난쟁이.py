import sys
def get_nums(nums):
    sum_n = sum(nums)
    for i in range(9):
        for j in range(i + 1, 9):
            if sum_n - nums[i] - nums[j] == 100:
                nums.pop(j)
                nums.pop(i)
                return nums


nums = [int(sys.stdin.readline()) for _ in range(9)]
print("\n".join([str(n) for n in get_nums(nums)]))