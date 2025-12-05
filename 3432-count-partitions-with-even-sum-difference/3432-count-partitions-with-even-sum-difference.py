class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        total = sum(nums)
        return 0 if total & 1 else len(nums) - 1