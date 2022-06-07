class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:
        @cache
        def helper(house: int, pcolor: int) -> int:
            if house == n:
                return 0
            
            cost = float('inf')
            for c in range(k):
                if c == pcolor:
                    continue
                cost = min(cost, costs[house][c] + helper(house + 1, c))
            return cost
        
        n, k = len(costs), len(costs[0])
        min_cost = float('inf')
        for c in range(k):
            min_cost = min(min_cost, helper(0, c))
        return min_cost