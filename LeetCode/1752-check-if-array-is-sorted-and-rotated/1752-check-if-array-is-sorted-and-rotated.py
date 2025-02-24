class Solution:
    def check(self, nums: List[int]) -> bool:
        length = len(nums)
        for i in range(length):
            rotated = [nums[(idx + i) % length] for idx in range(length)]
            if all(rotated[idx] <= rotated[idx + 1] for idx in range(length - 1)):
                return True
        return False