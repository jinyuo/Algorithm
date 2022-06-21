import sys
n, k = map(int, sys.stdin.readline().split())
li = list(map(int, sys.stdin.readline().split(',')))
for i in range(k):
    li = [li[i + 1] - li[i] for i in range(len(li) - 1)]
print(",".join([str(i) for i in li]))