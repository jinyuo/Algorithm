import sys
n = int(sys.stdin.readline())
li = [int(sys.stdin.readline()) for _ in range(n)]
c = [li[i + 1] - li[i] for i in range(n - 1)]
b = [li[i + 1] // li[i] for i in range(n - 1)]
print(li[n - 1] + c[0] if c.count(c[0]) == len(c) else li[n - 1] * b[0])