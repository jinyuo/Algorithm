class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        altitudes = [0]
        for i in gain:
            altitudes.append(altitudes[-1] + i)

        return max(altitudes)