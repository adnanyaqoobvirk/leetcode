class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        @cache
        def helper(pos: int, pick: bool) -> int:
            if pos == n:
                return 0 if pick else -inf
            
            if pick:
                return max(
                    nums[pos] + helper(pos + 1, True),
                    0
                )
            else:
                return max(
                    nums[pos] + helper(pos + 1, True),
                    helper(pos + 1, False)
                )
        n = len(nums)
        return helper(0, False)