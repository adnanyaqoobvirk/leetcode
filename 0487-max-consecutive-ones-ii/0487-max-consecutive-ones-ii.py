class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        zero_i = -1
        max_len = 0
        l = 0
        for r in range(len(nums)):
            if nums[r] == 0:
                max_len = max(max_len, r - l)
                if zero_i != -1:
                    l = zero_i + 1
                zero_i = r
        max_len = max(max_len, r - l + 1)
        return max_len