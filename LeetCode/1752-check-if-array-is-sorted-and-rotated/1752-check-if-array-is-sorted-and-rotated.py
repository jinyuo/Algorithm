class Solution:
    def check(self, nums: List[int]) -> bool:
        length = len(nums)
        for i in range(length):
            nums.append(nums.pop(0))
            if all(nums[idx] <= nums[idx + 1] for idx in range(length - 1)):
                return True
        return False