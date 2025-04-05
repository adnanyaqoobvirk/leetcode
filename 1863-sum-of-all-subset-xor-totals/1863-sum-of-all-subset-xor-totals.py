class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        ans = 0
        for s in range(1<<(len(nums))):
            xor = 0
            for i in range(len(nums)):
                if s & (1<<i):
                   xor ^= nums[i]
            ans += xor
        return ans