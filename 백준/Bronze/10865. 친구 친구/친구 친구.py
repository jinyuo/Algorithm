import sys

n, m = map(int, sys.stdin.readline().split())
students = [0 for _ in range(n)]
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    students[a - 1] += 1
    students[b - 1] += 1

print('\n'.join(str(i) for i in students))