class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        min_cost = 0
        l = 0
        for r in range(1, len(colors)):
            if colors[l] == colors[r]:
                if neededTime[l] < neededTime[r]:
                    min_cost += neededTime[l]
                    l = r
                else:
                    min_cost += neededTime[r]
            else:
                l = r
        return min_cost