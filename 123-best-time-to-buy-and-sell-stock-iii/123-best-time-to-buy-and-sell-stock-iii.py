class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        
        lprofits = []
        profit = 0
        price = prices[0]
        for p in prices:
            if p > price:
                profit = max(profit, p - price)
            else:
                price = p
            lprofits.append(profit)
        
        rprofits = [0]
        profit = 0
        price = prices[n - 1]
        for p in reversed(prices):
            if p < price:
                profit = max(profit, price - p)
            else:
                price = p
            rprofits.append(profit)
        
        profit = 0
        for i in range(n):
            profit = max(profit, lprofits[i] + rprofits[n - i - 1])
        
        return profit