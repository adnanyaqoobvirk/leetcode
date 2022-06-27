class Solution:
    def rob(self, nums: List[int]) -> int:
        @cache
        def helper(pos: int, first: bool) -> int:
            if first and pos >= n - 1:
                return 0
            
            if not first and pos >= n:
                return 0
            
            return max(
                nums[pos] + helper(pos + 2, first),
                helper(pos + 1, first)
            )
        n = len(nums)
        return max(
            nums[0] + helper(2, True),
            helper(1, False)
        )