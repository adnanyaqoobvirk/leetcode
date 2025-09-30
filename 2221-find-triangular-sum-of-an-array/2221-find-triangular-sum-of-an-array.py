class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        nCr = 1
        ans = 0
        n = len(nums) - 1
        for r, num in enumerate(nums):
            ans = (ans + num * nCr) % 10
            nCr = nCr * (n - r) // (r + 1)
        return ans