class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        if min(nums) < k:
            return -1
        
        nums = set(nums)
        nums.discard(k)
        return len(nums)