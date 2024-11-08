class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        ans = []
        xor = 0
        for num in nums:
            xor ^= num
            k = 0
            for i in range(maximumBit):
                pos = 1 << i
                if not (xor & pos):
                    k |= pos
            ans.append(k)
        ans.reverse()
        return ans