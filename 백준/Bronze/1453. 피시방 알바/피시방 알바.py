import sys
n = int(sys.stdin.readline())
s = sys.stdin.readline().split()
print(len(s) - len(set(s)))