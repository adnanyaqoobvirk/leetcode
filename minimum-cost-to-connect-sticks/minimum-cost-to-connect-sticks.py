class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        heapify(sticks)
        cost = 0
        while len(sticks) > 1:
            curr_cost = heappop(sticks) + heappop(sticks)
            cost += curr_cost
            heappush(sticks, curr_cost)
        return cost