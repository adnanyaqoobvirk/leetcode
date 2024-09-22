class Solution:
    def minCost(self, nums: List[int], cost: List[int]) -> int:
        nums_cost = sorted(zip(nums, cost))

        pfix_cost = [nums_cost[0][1]]
        for i in range(1, len(nums)):
            pfix_cost.append(pfix_cost[-1] + nums_cost[i][1])
        
        total_cost = 0
        for i in range(1, len(nums)):
            total_cost += nums_cost[i][1] * (nums_cost[i][0] - nums_cost[0][0])
        
        min_cost = total_cost
        curr_cost = total_cost
        for i in range(1, len(nums)):
            diff = nums_cost[i][0] - nums_cost[i - 1][0]
            curr_cost += diff * pfix_cost[i - 1]
            curr_cost -= diff * (pfix_cost[-1] - pfix_cost[i - 1])
            min_cost = min(min_cost, curr_cost)
        
        return min_cost