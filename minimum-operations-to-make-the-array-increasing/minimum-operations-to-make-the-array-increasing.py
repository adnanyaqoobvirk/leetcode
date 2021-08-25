class Solution:
    def minOperations(self, nums: List[int]) -> int:
        result = last = 0
        for num in nums:
            result += max(0, last - num + 1)
            last = max(num, last + 1)
        return result