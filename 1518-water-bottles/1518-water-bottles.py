class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        filled, empty = numBottles, 0
        ans = 0
        while filled > 0:
            ans += filled
            filled, empty = divmod(empty + filled, numExchange)
        return ans