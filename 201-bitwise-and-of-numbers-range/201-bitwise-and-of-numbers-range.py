class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        low = ceil(log2(left + 1)) if left else 0
        if (1 << low) >= right:
            ans = left
            for num in range(left + 1, right + 1):
                ans &= num
            return ans
        else:
            return 0