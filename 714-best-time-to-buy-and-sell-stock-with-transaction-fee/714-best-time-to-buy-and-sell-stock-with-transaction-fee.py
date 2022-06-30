class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        
        curr_bought = curr_not_bought = -inf
        for pos in reversed(range(n)):
            curr_bought, curr_not_bought = max(
                prices[pos],
                prices[pos] + curr_not_bought,
                curr_bought
            ), max(
                -prices[pos] - fee + curr_bought,
                curr_not_bought
            )
        return 0 if curr_not_bought < 0 else curr_not_bought