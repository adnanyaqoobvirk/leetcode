class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        ans = 0
        for i in range(2 ** len(nums)):
            xor = 0
            j = 0
            while i > 0:
                if i & 1:
                    xor ^= nums[j]
                i >>= 1
                j += 1
            ans += xor
        return ans