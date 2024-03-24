import sys
k = int(sys.stdin.readline())
cost = []
for _ in range(k):
    tmp = int(sys.stdin.readline())
    cost.pop() if tmp == 0 else cost.append(tmp)
print(sum(cost))