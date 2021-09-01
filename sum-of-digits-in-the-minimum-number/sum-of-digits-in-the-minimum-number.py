class Solution:
    def sumOfDigits(self, nums: List[int]) -> int:
        n = min(nums)
        res = 0
        while n > 0:
            n, d = divmod(n, 10)
            res += d
        return 0 if res & 1 else 1