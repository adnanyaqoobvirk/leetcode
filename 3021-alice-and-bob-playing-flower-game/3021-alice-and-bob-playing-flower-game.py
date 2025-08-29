class Solution:
    def flowerGame(self, n: int, m: int) -> int:
        xodd = (n + 1) // 2
        yeven = m // 2
        xeven = n // 2
        yodd = (m + 1) // 2
    
        return xodd * yeven + yodd * xeven