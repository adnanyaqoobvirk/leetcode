class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        
        profits = [0] * n
        profit = lprofit = rprofit = 0
        lprice, rprice = prices[0], prices[n - 1]
        for i in range(n):
            p = prices[i]
            if p > lprice:
                lprofit = max(lprofit, p - lprice)
            else:
                lprice = p
            
            p = prices[n - i - 1]
            if p < rprice:
                rprofit = max(rprofit, rprice - p)
            else:
                rprice = p
            
            profits[i] += lprofit
            profits[n - i - 1] += rprofit
            profit = max(profit, profits[i], profits[n - i - 1])
        
        return profit