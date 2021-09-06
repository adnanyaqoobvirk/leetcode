class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        xor = nums[0]
        for j in range(1, len(nums)):
            xor ^= nums[j]
            
        ans = []
        mx = (1 << maximumBit) - 1
        for i in range(len(nums) - 1, -1, -1):
            ans.append(mx ^ xor)
            xor ^= nums[i]
        return ans