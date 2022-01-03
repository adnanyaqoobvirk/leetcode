class Solution:
    def maxVacationDays(self, flights: List[List[int]], days: List[List[int]]) -> int:
        @cache
        def helper(city: int, week: int) -> int:
            if week == k:
                return 0
            
            max_vacs = 0
            for i in range(n):
                if flights[city][i] or i == city:
                    max_vacs = max(max_vacs, days[i][week] + helper(i, week + 1))
        
            return max_vacs
        
        k, n = len(days[0]), len(flights[0])
        return helper(0, 0)