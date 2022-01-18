class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        ans, fl = 0, len(flowerbed)
        for i in range(len(flowerbed)):
            if flowerbed[i] == 0 and (i == 0 or flowerbed[i - 1] == 0) and (i == fl - 1 or flowerbed[i + 1] == 0):
                    flowerbed[i] = 1
                    ans += 1
        return ans >= n