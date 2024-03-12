import sys
n = int(sys.stdin.readline())
print(sum([n * i + i for i in range(1, n)]))