import sys
e, s, m = map(int, sys.stdin.readline().split())
y = (6916 * e + 4845 * s + 4200 * m) % 7980
print(y if y else 7980)