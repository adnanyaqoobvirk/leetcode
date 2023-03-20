class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        m = len(flowerbed)
        for i in range(m):
            if flowerbed[i] == 1:
                continue
                
            if i - 1 >= 0 and flowerbed[i - 1] == 1:
                continue
            
            if i + 1 < m and flowerbed[i + 1] == 1:
                continue
            
            n -= 1
            flowerbed[i] = 1
        return n <= 0