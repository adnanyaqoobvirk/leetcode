class Solution:
    def minCost(self, costs: List[List[int]]) -> int:    
        prev, curr = [0] * 3, [0] * 3
        for i in range(len(costs)):
            for j in range(3):
                cost = float('inf')
                for k in range(3):
                    if k != j:
                        cost = min(cost, costs[i][k] + prev[k])
                curr[j] = cost
            prev, curr = curr, prev
        return min(prev)