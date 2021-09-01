class Solution:
    def sumOfDigits(self, nums: List[int]) -> int:
        n = min(nums)
        res = 0
        while n > 0:
            n, d = divmod(n, 10)
            res += d
        return res & 1 ^ 1