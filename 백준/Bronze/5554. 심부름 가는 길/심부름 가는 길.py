import sys
s = sum([int(sys.stdin.readline()) for _ in range(4)])
print(s // 60, s % 60, sep="\n")