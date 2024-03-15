import sys

N = int(sys.stdin.readline())
A = set(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))
intersection = A & set(nums)
print("\n".join(['1' if n in intersection else '0' for n in nums]))