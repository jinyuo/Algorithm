import sys
n = int(sys.stdin.readline())
li = list(map(int, sys.stdin.readline().split()))
order = list()
for i in range(1, n + 1):
    order.insert(len(order) - li[i - 1], i)
print(*order)