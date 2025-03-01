from itertools import groupby

class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        flags = ['+' if nums[i] < nums[i + 1] else ('-' if nums[i] > nums[i+ 1] else '=') for i in range(len(nums) - 1)]
        flags = [len(list(l)) for f, l in groupby(flags) if f != '=']
        
        if flags:
            return max(flags) + 1
        else:
            return 1
        