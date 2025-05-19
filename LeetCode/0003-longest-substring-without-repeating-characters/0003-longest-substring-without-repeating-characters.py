class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start, end = 0, 0
        max_length = 0
        while end < len(s):
            substring = s[start:end]
            if s[end] not in substring:
                end += 1
                max_length = max(max_length, end - start)
            else:
                start = end
                end = start

        return max_length