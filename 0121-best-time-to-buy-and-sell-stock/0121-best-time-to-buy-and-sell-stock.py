class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        bought = unbought = -inf
        for i in reversed(range(len(prices))):
            bought, unbought = max(
                prices[i],
                bought
            ), max(
                unbought,
                bought - prices[i]
            )
        return 0 if unbought < 0 else unbought