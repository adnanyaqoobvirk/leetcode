class Solution:
    def maxDistinctElements(self, nums: List[int], k: int) -> int:
        nums.sort()
        
        taken = -inf
        distincts = 0
        for num in nums:
            min_not_taken = max(taken + 1, num - k)
            if min_not_taken <= num + k:
                distincts += 1
                taken = min_not_taken
        return distincts