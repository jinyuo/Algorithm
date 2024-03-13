import sys
import math
num = [int(sys.stdin.readline()) for _ in range(5)]
print(num[0] - max([math.ceil(num[1] / num[3]), math.ceil(num[2] / num[4])]))