class Solution:
    def minCost(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:
        @cache
        def helper(i: int, nhs: int, pcolor: int) -> int:
            if i == m:
                return inf if nhs != 0 else 0
            
            if nhs < 0:
                return inf
            
            if houses[i] != 0:
                return helper(
                    i + 1, 
                    nhs - 1 if pcolor != houses[i] else nhs,
                    houses[i]
                )
            
            ans = inf
            for j in range(n):
                ans = min(
                    ans, 
                    cost[i][j] + helper(
                        i + 1, 
                        nhs - 1 if pcolor != j + 1 else nhs,
                        j + 1
                    )
                )
            return ans
        res = helper(0, target, 0)
        return -1 if res == inf else res