class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        pdiff, seq_len = 0, 1
        for i in range(1, len(nums)):
            diff = nums[i] - nums[i - 1]
            if diff == 0 or (diff < 0 and pdiff < 0) or (diff > 0 and pdiff > 0):
                continue
            pdiff, seq_len = diff, seq_len + 1
        return seq_len