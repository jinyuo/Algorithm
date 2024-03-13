import sys

burger = [int(sys.stdin.readline()) for _ in range(3)]
beverage = [int(sys.stdin.readline()) for _ in range(2)]
print(min(burger) + min(beverage) - 50)