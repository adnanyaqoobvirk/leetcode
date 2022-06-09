class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:
        n, k = len(costs), len(costs[0])
        prev, curr = [-1, 0, 0], [-1, float('inf'), float('inf')]
        for house in reversed(range(n)):
            for rc in range(k):
                if rc != prev[0]:
                      curr_val = costs[house][rc] + prev[1]
                else:
                      curr_val = costs[house][rc] + prev[2]
                if curr_val < curr[1]:
                    curr = [rc, curr_val, curr[1]]
                elif curr_val < curr[2]:
                    curr[2] = curr_val
            prev, curr = curr, [-1, float('inf'), float('inf')]
        return prev[1]