class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        l = ans = zero = 0
        for r in range(len(nums)):
            if nums[r] == 0:
                if zero:
                    ans = max(ans, r - l)
                    while nums[l] != 0:
                        l += 1
                    l += 1
                zero = 1
        return max(ans, len(nums) - l)