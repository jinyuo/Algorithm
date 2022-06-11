import sys
from heapq import heappush
from heapq import heappop
n = int(sys.stdin.readline())
p_nums = []
n_nums = []
for _ in range(n):
    i = int(sys.stdin.readline())
    if i != 0:
        if i > 0:
            heappush(p_nums, i)
        else:
            heappush(n_nums, -1 * i)
    else:
        if not p_nums and not n_nums:
            print(0)
        else:
            if not n_nums:
                print(heappop(p_nums))
            elif not p_nums:
                print(-1 * heappop(n_nums))
            elif p_nums[0] == n_nums[0]:
                print(-1 * heappop(n_nums))
            elif p_nums[0] > n_nums[0]:
                print(-1 * heappop(n_nums))
            else:
                print(heappop(p_nums))