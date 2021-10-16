class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        profit = 0
        price = prices[0]
        for i in range(1, n):
            if prices[i] > price:
                profit = max(profit, prices[i] - price)
            elif prices[i] < price:
                price = prices[i]
        return profit