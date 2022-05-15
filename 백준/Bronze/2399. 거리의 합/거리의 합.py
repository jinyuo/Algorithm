n = int(__import__('sys').stdin.readline())
nums = list(map(int, __import__('sys').stdin.readline().split()))
s = 0
for i in nums:
    for j in nums:
        s += abs(j - i)
print(s)