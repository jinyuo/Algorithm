import sys
def prime(n):
    nums = [True for _ in range(n + 1)]
    nums[0] = False
    nums[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        if nums[i]:
            for j in range(i + i, n + 1, i):
                nums[j] = False
    return nums


nums = []
while True:
    n = int(sys.stdin.readline())
    if n == 0:
        break
    nums.append(n)

p_nums = prime(max(nums) * 2)
for n in nums:
    print(len([i for i in p_nums[n + 1:2 * n + 1] if i == True]))