class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        total = 0
        for i in range(1, 1 << len(nums)):
            xor = 0
            for j in range(len(nums)):
                if (1 << j) & i:
                    xor ^= nums[j]
            total += xor
        return total