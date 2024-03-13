import sys
n_list = [int(sys.stdin.readline()) for _ in range(28)]
for i in range(1, 31):
    if i not in n_list:
        print(i)