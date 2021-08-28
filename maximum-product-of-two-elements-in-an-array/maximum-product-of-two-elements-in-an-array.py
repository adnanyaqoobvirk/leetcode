class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        mx, smx = 0, 0
        for num in nums:
            if mx <= num:
                smx, mx = mx, num
            elif smx <= num:
                smx = num
        return (mx - 1) * (smx - 1)