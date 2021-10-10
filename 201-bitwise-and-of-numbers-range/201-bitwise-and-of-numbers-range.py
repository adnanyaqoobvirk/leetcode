class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        count = 0
        while left != 0 and left != right:
            left >>= 1
            right >>= 1
            count += 1
        return left << count