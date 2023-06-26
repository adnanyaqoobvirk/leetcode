class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        unique = [k for k, v in Counter(nums).items() if v == 1]
        return max(unique) if unique else -1