class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        val = sum(nums[:k])
        max_val = val

        for i in range(len(nums) - k):
            val = val - nums[i] + nums[i + k]
            if val > max_val:
                max_val = val
        return max_val / k
