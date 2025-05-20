

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result = []
        window = deque()
        for i, num in enumerate(nums):
            # 정렬
            while window and window[-1] < num:
                window.pop()
            window.append(num)
            
            # 윈도우 바깥 원소 처리
            if i >= k and nums[i - k] == window[0]:
                window.popleft()

            if i >= k - 1:
                result.append(window[0])
        return result