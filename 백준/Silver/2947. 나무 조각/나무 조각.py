import sys
li = list(map(int, sys.stdin.readline().split()))
while li != [1, 2, 3, 4, 5]:
    for i in range(4):
        if li[i] > li[i + 1]:
            li[i], li[i + 1] = li[i + 1], li[i]
            print(*li)
