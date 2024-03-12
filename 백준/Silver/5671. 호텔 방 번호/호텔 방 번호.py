import sys
while True:
    try:
        n, m = map(int, sys.stdin.readline().split())
    except:
        break

    cnt = 0
    for i in range(n, m + 1):
        li = list(str(i))
        if len(li) == len(set(li)):
            cnt += 1
    print(cnt)