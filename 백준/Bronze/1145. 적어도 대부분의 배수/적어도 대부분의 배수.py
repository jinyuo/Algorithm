import sys
import math
from itertools import combinations

nums = list(map(int, sys.stdin.readline().strip().split()))
print(min([math.lcm(*n) for n in combinations(nums, 3)]))