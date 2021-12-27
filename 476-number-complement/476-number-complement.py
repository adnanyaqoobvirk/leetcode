class Solution:
    def findComplement(self, num: int) -> int:
        ans = count = 0
        while num > 0:
            if not (num & 1): ans |= (1 << count)
            num >>= 1
            count += 1
        return ans