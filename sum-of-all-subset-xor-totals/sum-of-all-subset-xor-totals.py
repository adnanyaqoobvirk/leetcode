class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        bits = 0
        for num in nums:
            bits |= num
        return (1 << len(nums) - 1) * bits