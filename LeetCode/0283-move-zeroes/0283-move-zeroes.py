class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        none_zeros = [n for n in nums if n != 0]
        length_none_zeros = len(none_zeros)
 
        for i in range(length):
            if i < length_none_zeros:
                nums[i] = none_zeros[i]
            else:
                nums[i] = 0
 