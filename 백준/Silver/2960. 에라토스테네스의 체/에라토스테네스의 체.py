import sys
n, k = map(int, sys.stdin.readline().split())
nums = [i for i in range(2, n + 1)]
cnt = 0
while nums:
    p = nums.pop(0)
    cnt += 1
    if cnt == k:
        print(p)
        exit()
    for i in nums:
        if i % p == 0:
            nums.remove(i)
            cnt += 1
            if cnt == k:
                print(i)
                exit()