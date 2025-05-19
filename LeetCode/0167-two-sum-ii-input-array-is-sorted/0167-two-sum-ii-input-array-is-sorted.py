class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        start, end = 0, len(numbers) - 1

        while start < end:
            twosum = numbers[start] + numbers[end]
            if twosum == target:
                return [start + 1, end + 1]
            elif twosum > target:
                end -= 1
            elif twosum < target:
                start += 1
