import sys
n = int(sys.stdin.readline())
t = list(map(int, sys.stdin.readline().split()))
i = n - 1
while i > 0 and t[i - 1] > t[i]:
    i -= 1
if i <= 0:
    print(-1)
    exit()

j = n - 1
while t[j] < t[i - 1]:
    j -= 1
t[i - 1], t[j] = t[j], t[i - 1]
print(*(t[:i] + t[i:][::-1]))