class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)
        
        prefixes = []
        prefix = 0
        for i in reversed(range(n)):
            prefixes.append(prefix)
            prefix += nums[i]
        
        prefix = 0
        for i in range(n):
            if prefix == prefixes[n - i - 1]:
                return i
            prefix += nums[i]
        
        return -1