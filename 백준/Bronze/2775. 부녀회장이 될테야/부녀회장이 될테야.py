import sys
fl = [[]]
for i in range(15):
    if i == 0:
        fl[0] = [h + 1 for h in range(14)]
    else:
        fl.append([sum(fl[i - 1][:h + 1]) for h in range(14)])

t = int(sys.stdin.readline())
for _ in range(t):
    k = int(sys.stdin.readline())
    n = int(sys.stdin.readline())
    print(fl[k][n - 1])