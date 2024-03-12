import sys
while True:
    li = list(map(int, sys.stdin.readline().split()))
    if li[0] == li[1] == li[2] == li[3] == 0:
        exit()

    cnt = 0
    while not li[0] == li[1] == li[2] == li[3]:
        li = [abs(li[0] - li[1]), abs(li[1] - li[2]), abs(li[2] - li[3]), abs(li[3] - li[0])]
        cnt += 1
    print(cnt)