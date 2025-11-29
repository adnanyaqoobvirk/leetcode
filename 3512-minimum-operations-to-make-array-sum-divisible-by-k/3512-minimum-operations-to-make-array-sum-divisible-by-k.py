class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        r = 0
        for num in nums:
            r += num
            r %= k
        return r