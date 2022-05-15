n = int(__import__('sys').stdin.readline())
nums = list(map(int, __import__('sys').stdin.readline().split()))
nums.sort()
s = 0
for i in range(n - 1):
    for j in range(i + 1, n):
        s += 2 * (nums[j] - nums[i])
print(s)
