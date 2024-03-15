import sys

N = int(sys.stdin.readline())
A = set(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))
set_num = set(nums)
intersection = A & set_num
for n in nums:
    print(1 if n in intersection else 0)