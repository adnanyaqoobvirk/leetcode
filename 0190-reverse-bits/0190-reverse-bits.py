class Solution:
    def reverseBits(self, n: int) -> int:
        ans = 0
        for i in range(32):
            ans |= int((n & (1 << i)) > 0) << (31 - i)
        return ans