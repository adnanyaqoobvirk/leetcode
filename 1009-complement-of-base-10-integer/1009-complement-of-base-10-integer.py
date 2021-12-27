class Solution:
    def bitwiseComplement(self, n: int) -> int:
        if n == 0:
            return 1
        
        ans = count = 0
        while n > 0:
            if not (n & 1): ans |= (1 << count)
            n >>= 1
            count += 1
        return ans