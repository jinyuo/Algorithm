import sys
a, b = sys.stdin.readline()[::-1].split()
print(a if a > b else b)