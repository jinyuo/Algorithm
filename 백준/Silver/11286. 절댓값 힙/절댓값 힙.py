import sys
import heapq
n = int(sys.stdin.readline())
p_nums = []
n_nums = []
for _ in range(n):
    n = int(sys.stdin.readline())
    if n != 0:
        if n > 0:
            heapq.heappush(p_nums, n)
        else:
            heapq.heappush(n_nums, -1 * n)
    else:
        if not p_nums and not n_nums:
            print(0)
        else:
            if not n_nums:
                print(heapq.heappop(p_nums))
            elif not p_nums:
                print(-1 * heapq.heappop(n_nums))
            elif p_nums[0] == n_nums[0]:
                print(-1 * heapq.heappop(n_nums))
            elif p_nums[0] > n_nums[0]:
                print(-1 * heapq.heappop(n_nums))
            else:
                print(heapq.heappop(p_nums))