class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()
        
        n = len(nums)
        
        if n & 1:
            median = nums[n // 2]
        else:
            median = (nums[n // 2 - 1] + nums[n // 2]) // 2
        
        ans = 0
        for num in nums:
            ans += abs(median - num)
        return ans