class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        @cache
        def dp(i: int, aur: int) -> int:
            if aur == maur:
                return 2**(n - i)

            if i >= n:
                return 0

            return dp(i + 1, aur | nums[i]) + dp(i + 1, aur)
        n = len(nums)
        maur = 0
        for num in nums:
            maur |= num
        return dp(0, 0)