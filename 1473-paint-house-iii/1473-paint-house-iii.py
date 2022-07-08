class Solution:
    def minCost(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:
        prev = [[inf] * (n + 1) for _ in range(target + 2)]
        curr = [[inf] * (n + 1) for _ in range(target + 2)]
        for i in reversed(range(m + 1)):
            for nhs in reversed(range(target + 1)):
                for pcolor in reversed(range(n + 1)):
                    if i == m:
                        curr[nhs][pcolor] = inf if nhs != target else 0
                        continue
                        
                    if houses[i] != 0:
                        curr[nhs][pcolor] = prev[
                            nhs + 1 if pcolor != houses[i] else nhs
                        ][houses[i]]
                        continue

                    for j in range(n):
                        curr[nhs][pcolor] = min(
                            curr[nhs][pcolor], 
                            cost[i][j] + prev[
                                nhs + 1 if pcolor != j + 1 else nhs
                            ][j + 1]
                        )
            prev, curr = curr, [[inf] * (n + 1) for _ in range(target + 2)]
        return prev[0][0] if prev[0][0] != inf else -1