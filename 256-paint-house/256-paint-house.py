class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        @cache
        def helper(pos: int, prev: int) -> int:
            if pos >= len(costs):
                return 0
            
            cost = float('inf')
            for i in range(3):
                if i != prev:
                    cost = min(cost, costs[pos][i] + helper(pos + 1, i))
            return cost
        return helper(0, -1)