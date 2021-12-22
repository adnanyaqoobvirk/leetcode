class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ans = curr = 0
        for num in nums:
            if not num:
                ans = max(ans, curr)
                curr = 0
            else:
                curr += 1
        return max(ans, curr)