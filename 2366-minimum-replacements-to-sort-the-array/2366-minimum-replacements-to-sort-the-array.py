class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        res, prev = 0, inf
        for curr in reversed(nums):
            if prev >= curr:
                prev = curr
            else:
                ops, r = divmod(curr, prev)
                if r > 0:
                    res += ops
                    prev = curr // (ops + 1)
                else:
                    res += ops - 1
        return res