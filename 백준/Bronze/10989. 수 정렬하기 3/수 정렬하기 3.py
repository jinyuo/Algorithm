import sys

N = int(sys.stdin.readline())
list_nums = [0 for _ in range(10000)]
for _ in range(N):
    list_nums[int(sys.stdin.readline()) - 1] += 1
list_nums = [(i + 1, cnt) for i, cnt in enumerate(list_nums) if cnt > 0]
for i, cnt in list_nums:
    for _ in range(cnt):
        print(i)