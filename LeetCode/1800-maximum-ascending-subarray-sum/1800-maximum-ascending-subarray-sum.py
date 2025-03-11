class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        list_sum = []
        s = 0
        for i in range(len(nums) - 1):
            s += nums[i]
            if nums[i] >= nums[i + 1]:
                list_sum.append(s)
                s = 0
        list_sum.append(s + nums[-1])
        return max(list_sum)