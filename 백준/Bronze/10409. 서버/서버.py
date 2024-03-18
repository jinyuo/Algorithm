import sys
n, t = map(int, sys.stdin.readline().split())
p_list = list(map(int, sys.stdin.readline().split()))
for i in range(n, -1, -1):
    tmp = p_list[:i]
    if sum(tmp) <= t:
        print(len(tmp))
        exit()
