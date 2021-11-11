class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        rsum = minimum = 0
        for num in nums:
            rsum += num
            minimum = min(rsum, minimum)
        return abs(minimum) + 1
        