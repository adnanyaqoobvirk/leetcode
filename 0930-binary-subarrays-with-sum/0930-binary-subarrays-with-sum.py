class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        def atMost(s):
            total = count = lo = 0
            for hi in range(len(nums)):
                total += nums[hi]
                while lo <= hi and total > s:
                    total -= nums[lo]
                    lo += 1
                count += hi - lo + 1
            return count
        return atMost(goal) - atMost(goal - 1)