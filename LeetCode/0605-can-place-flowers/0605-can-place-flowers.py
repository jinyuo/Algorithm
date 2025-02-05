class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        length = len(flowerbed)
        for i, f in enumerate(flowerbed):
            if all([d == 0 for d in flowerbed[max(0, i - 1):min(i + 2, length)]]):
                flowerbed[i] = 1
                n -= 1
            if n <= 0:
                return True
        return False