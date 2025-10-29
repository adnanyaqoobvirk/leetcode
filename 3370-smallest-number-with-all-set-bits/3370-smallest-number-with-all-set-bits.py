class Solution:
    def smallestNumber(self, n: int) -> int:
        ans = 0
        for _ in range(n.bit_length()):
            ans = (ans << 1) | 1
        return ans