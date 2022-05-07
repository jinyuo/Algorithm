import sys
abc = list(map(int, sys.stdin.readline().split()))
print(max([abc[1] - abc[0], abc[2] - abc[1]]) - 1)