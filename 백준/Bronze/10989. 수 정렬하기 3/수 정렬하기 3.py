import sys

N = int(sys.stdin.readline())
list_nums = [0 for _ in range(10000)]
for _ in range(N):
    list_nums[int(sys.stdin.readline()) - 1] += 1
for i, cnt in enumerate(list_nums):
    for _ in range(list_nums[i]):
        print(i + 1)