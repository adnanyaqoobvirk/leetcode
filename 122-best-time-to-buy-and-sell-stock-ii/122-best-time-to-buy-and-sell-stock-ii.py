class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        
        curr_bought = curr_not_bought = -inf
        for pos in reversed(range(n)):
            curr_bought, curr_not_bought = max(
                prices[pos],
                curr_bought,
                prices[pos] + curr_not_bought
            ), max(
                -prices[pos] + curr_bought,
                curr_not_bought
            )
        return 0 if curr_not_bought < 0 else curr_not_bought