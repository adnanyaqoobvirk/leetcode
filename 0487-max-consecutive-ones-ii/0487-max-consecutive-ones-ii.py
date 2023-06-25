class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        l = ans = 0
        zero = -1
        for r in range(len(nums)):
            if nums[r] == 0:
                ans = max(ans, r - l)
                l = zero + 1
                zero = r
        return max(ans, len(nums) - l)