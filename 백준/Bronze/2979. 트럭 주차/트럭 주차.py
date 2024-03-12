import sys
t = []
p_cost = list(map(int, sys.stdin.readline().split()))
c = 0
for _ in range(3):
    arrival, depart = map(int, sys.stdin.readline().split())
    if len(t) < depart:
        t += [0] * (depart - len(t))
    for i in range(arrival, depart):
        t[i] += 1
for i in range(1, 4):
    c += i * t.count(i) * p_cost[i - 1]
print(c)