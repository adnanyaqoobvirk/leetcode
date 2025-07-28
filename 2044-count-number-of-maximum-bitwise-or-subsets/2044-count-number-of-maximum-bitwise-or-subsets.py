class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        n = len(nums)
        maur = 0
        for num in nums:
            maur |= num
        
        dp = [0] * (1 << maur.bit_length())
        dp[maur] = 1
        for i in reversed(range(n)):
            for aur in range(maur + 1):
                dp[aur] += dp[aur | nums[i]]
        return dp[0]