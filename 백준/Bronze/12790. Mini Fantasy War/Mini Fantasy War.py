import sys

t = int(sys.stdin.readline())
list_weight = [(1, 1), (1, 5), (0, 2), (None, 2)]

for i in range(t):
    list_spec = list(map(int, sys.stdin.readline().split()))
    idx = 4
    list_spec = [list_spec[i] + list_spec[idx + i] for i in range(idx)]
    list_weight[-1] = (list_spec[-1], list_weight[-1][1])
    list_spec = [max(list_spec[i], list_weight[i][0]) * list_weight[i][1] for i in range(idx)]
    print(sum(list_spec))