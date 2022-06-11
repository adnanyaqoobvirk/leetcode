class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        n = len(days)
        dp = [0] * (n + 30)
        for pos in reversed(range(n)):
            one_day_cost = costs[0] + dp[pos + 1]
            
            seven_day_cost = costs[1]
            seventh_day = days[pos] + 6
            npos = pos
            while npos < n and days[npos] <= seventh_day:
                npos += 1
            seven_day_cost += dp[npos]
            
            thirty_day_cost = costs[2]
            thirty_day = days[pos] + 29
            npos = pos
            while npos < n and days[npos] <= thirty_day:
                npos += 1
            thirty_day_cost += dp[npos]
        
            dp[pos] = min(
                one_day_cost,
                seven_day_cost,
                thirty_day_cost
            )
        return dp[0]