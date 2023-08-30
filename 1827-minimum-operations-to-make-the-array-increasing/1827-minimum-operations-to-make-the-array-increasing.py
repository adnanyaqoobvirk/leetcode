class Solution:
    def minOperations(self, nums: List[int]) -> int:
        res = prev = 0
        for curr in nums:
            if curr <= prev:
                res += prev - curr + 1
                prev += 1
            else:
                prev = curr
        return res