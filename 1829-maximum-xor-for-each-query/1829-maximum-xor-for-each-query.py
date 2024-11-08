class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        ans = []
        k = (1 << maximumBit) - 1
        for num in nums:
            k ^= num
            ans.append(k)
        ans.reverse()
        return ans