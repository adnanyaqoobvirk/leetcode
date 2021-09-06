class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        xor = 0
        for num in nums:
            xor ^= num
            
        ans = []
        mx = (1 << maximumBit) - 1
        for num in reversed(nums):
            ans.append(mx ^ xor)
            xor ^= num
        return ans