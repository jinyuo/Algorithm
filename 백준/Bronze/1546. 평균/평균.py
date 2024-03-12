import sys
n = int(sys.stdin.readline())
s = list(map(int, sys.stdin.readline().split()))
s = [i * 100 / max(s) for i in s]
print(sum(s)/n)