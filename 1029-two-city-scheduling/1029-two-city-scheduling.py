class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs.sort(key=lambda x: x[0] - x[1])
        total_cost, n = 0, len(costs) // 2
        for i in range(len(costs)):
            acost, bcost = costs[i]
            total_cost += acost if i < n else bcost
        return total_cost