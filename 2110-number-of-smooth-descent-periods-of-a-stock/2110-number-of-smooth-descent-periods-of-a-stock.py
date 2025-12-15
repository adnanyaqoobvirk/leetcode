class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        descent_length = 1
        period_count = 0
        for i in range(1, len(prices)):
            if prices[i - 1] - prices[i] != 1:
                period_count += descent_length * (descent_length + 1) // 2
                descent_length = 1
            else:
                descent_length += 1
        
        last_descent_count = descent_length * (descent_length + 1) // 2
        period_count += last_descent_count
        return period_count