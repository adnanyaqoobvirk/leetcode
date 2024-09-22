class Solution:
    def minCost(self, nums: List[int], cost: List[int]) -> int:
        def baseCost(base: int) -> int:
            ans = 0
            for i in range(len(nums)):
                ans += abs(nums[i] - base) * cost[i]
            return ans

        min_cost = 0
        lo, hi = min(nums) - 1, max(nums)
        while lo + 1 < hi:
            mid = lo + (hi - lo) // 2

            cost1 = baseCost(mid)
            cost2 = baseCost(mid + 1)

            if cost1 <= cost2:
                hi = mid
                min_cost = cost1
            else:
                lo = mid
                min_cost = cost2
        return min_cost