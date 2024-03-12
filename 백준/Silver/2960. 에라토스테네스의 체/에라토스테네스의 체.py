import sys
n, k = map(int, sys.stdin.readline().split())
nums = [i for i in range(2, n + 1)]
ord = []
while nums:
    p = nums.pop(0)
    ord.append(p)
    for i in nums:
        if i % p == 0:
            ord.append(i)
            nums.remove(i)

    if len(ord) >= k:
        print(ord[k - 1])
        exit()