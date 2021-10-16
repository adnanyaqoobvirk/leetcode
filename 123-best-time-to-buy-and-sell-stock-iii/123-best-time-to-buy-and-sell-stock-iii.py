class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        
        lprofits = [0]
        profit = 0
        price = prices[0]
        for i in range(1, n):
            if prices[i] > price:
                profit = max(profit, prices[i] - price)
            else:
                price = prices[i]
            
            lprofits.append(profit)
        
        rprofits = [0]
        profit = 0
        price = prices[n - 1]
        for i in reversed(range(n - 1)):
            if prices[i] < price:
                profit = max(profit, price - prices[i])
            else:
                price = prices[i]
            
            rprofits.append(profit)
        
        profit = 0
        for i in range(n):
            profit = max(profit, lprofits[i] + rprofits[n - i - 1])
        
        return profit