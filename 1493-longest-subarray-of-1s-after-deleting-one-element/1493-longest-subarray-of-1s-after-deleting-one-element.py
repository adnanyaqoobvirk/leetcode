class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        curr_zero = -1
        zeros = ans = next_zero = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                if zeros == 1:
                    ans = max(ans, i - curr_zero - 2)
                    zeros = 1
                    curr_zero = next_zero
                    next_zero = i
                else:
                    zeros += 1
                    next_zero = i
        ans = max(ans, len(nums) - curr_zero - 2)
        return ans if ans != len(nums) else ans - 1