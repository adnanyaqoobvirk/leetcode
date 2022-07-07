class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        @cache
        def helper(pos: int, m: int) -> int:
            if pos >= m:
                return 0
            
            return max(
                nums[pos] + helper(pos + 2, m),
                helper(pos + 1, m)
            )
        n = len(nums)
        return max(
            helper(0, n - 1),
            helper(1, n)
        )