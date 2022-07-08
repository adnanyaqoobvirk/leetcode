class Solution:
    def minCost(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:
#         @cache
#         def helper(i: int, nhs: int, pcolor: int) -> int:
#             if i == m:
#                 return inf if nhs != target else 0
            
#             if houses[i] != 0:
#                 return helper(
#                     i + 1, 
#                     nhs + 1 if pcolor != houses[i] else nhs,
#                     houses[i]
#                 )
            
#             ans = inf
#             for j in range(n):
#                 ans = min(
#                     ans, 
#                     cost[i][j] + helper(
#                         i + 1, 
#                         nhs + 1 if pcolor != j + 1 else nhs,
#                         j + 1
#                     )
#                 )
#             return ans
#         res = helper(0, 0, 0)
#         return -1 if res == inf else res
    
        dp = [
            [[inf] * (n + 1) for _ in range(target + 2)]
            for _ in range(m + 1)
        ]
    
        for i in reversed(range(m + 1)):
            for nhs in reversed(range(target + 1)):
                for pcolor in reversed(range(n + 1)):
                    if i == m:
                        dp[i][nhs][pcolor] = inf if nhs != target else 0
                        continue
                        
                    if houses[i] != 0:
                        dp[i][nhs][pcolor] = dp[i + 1][
                            nhs + 1 if pcolor != houses[i] else nhs
                        ][houses[i]]
                        continue

                    for j in range(n):
                        dp[i][nhs][pcolor] = min(
                            dp[i][nhs][pcolor], 
                            cost[i][j] + dp[i + 1][
                                nhs + 1 if pcolor != j + 1 else nhs
                            ][j + 1]
                        )
        return dp[0][0][0] if dp[0][0][0] != inf else -1