import sys
import heapq
n = int(sys.stdin.readline())
nums = []
ab_nums = []
for _ in range(n):
    n = int(sys.stdin.readline())
    if n != 0:
        nums.append(n)
        heapq.heappush(ab_nums, abs(n))
    else:
        if len(ab_nums) == 0:
            print(0)
        else:
            i = heapq.heappop(ab_nums)
            if -1 * i in nums:
                nums.remove(-1 * i)
                print(-1 * i)
            else:
                nums.remove(i)
                print(i)