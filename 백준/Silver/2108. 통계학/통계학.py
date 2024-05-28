import sys
from collections import Counter

N = int(sys.stdin.readline())
list_num = [int(sys.stdin.readline()) for _ in range(N)]
list_num.sort()
cnt = Counter(list_num).most_common()
max_cnt = max([c for v, c in cnt])
freq_nums = [v for v, c in cnt if c == max_cnt]

print(round((sum(list_num) / N)))
print((list_num[N // 2] + list_num[N // 2 - 1]) / 2 if N % 2 == 0 else list_num[N // 2])
print(freq_nums[min(1, len(freq_nums) - 1)])
print(list_num[-1] - list_num[0])