class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        @cache
        def helper(pos: int, ppos: int, psign: bool) -> int:
            if pos == n:
                return 1
            
            diff = nums[pos] - nums[ppos]
            if diff == 0 or (diff > 0 if psign else diff < 0):
                return helper(pos + 1, ppos, psign)
            else:
                return max(
                    1 + helper(pos + 1, pos, diff > 0),
                    helper(pos + 1, pos, True),
                    helper(pos + 1, pos, False)
                )
        n = len(nums)
        return max(helper(1, 0, True), helper(1, 0, False))