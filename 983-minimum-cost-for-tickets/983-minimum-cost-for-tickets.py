class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        @cache
        def helper(pos: int) -> int:
            if pos >= n:
                return 0
            
            one_day_cost = costs[0] + helper(pos + 1)
            
            seven_day_cost = costs[1]
            seventh_day = days[pos] + 6
            npos = pos
            while npos < n and days[npos] <= seventh_day:
                npos += 1
            seven_day_cost += helper(npos)
            
            thirty_day_cost = costs[2]
            thirty_day = days[pos] + 29
            npos = pos
            while npos < n and days[npos] <= thirty_day:
                npos += 1
            thirty_day_cost += helper(npos)
        
            return min(
                one_day_cost,
                seven_day_cost,
                thirty_day_cost
            )
        
        n = len(days)
        return helper(0)