import sys
num = sorted([int(sys.stdin.readline()) for _ in range(5)])
print(sum(num) // 5)
print(num[2])