class Solution:
    def minCost(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:
        @cache
        def helper(house: int, nei: int, pc: int) -> int:
            if nei < 0:
                return inf
            
            if house == m:
                return 0 if nei == 0 else inf
            
            if houses[house] != 0:
                return helper(
                    house + 1, 
                    (nei if pc == houses[house] - 1 else nei - 1), 
                    houses[house] - 1
                )
            
            min_cost = inf
            for c in range(n):
                min_cost = min(
                    min_cost,
                    cost[house][c] + helper(house + 1, (nei if pc == c else nei - 1), c)
                )
            return min_cost
        
        res = helper(0, target, -1)
        return -1 if res == inf else res