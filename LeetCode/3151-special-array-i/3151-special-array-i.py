class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        length = len(nums)
        nums = list(map(lambda x: x % 2, nums))
        return all(nums[i] != nums[i + 1] for i in range(length - 1)) or length == 1