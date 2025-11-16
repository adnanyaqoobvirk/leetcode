class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_val = 0
        ans = 0
        for v in reversed(prices):
            ans = max(ans, max_val - v)
            max_val = max(max_val, v)
        return ans