class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n = len(nums)
        
        if n <= 1:
            return n
        
        nums.sort()
        
        ans = 0
        count = 1
        for i in range(1, n):
            diff = nums[i] - nums[i - 1]
            if diff == 1:
                count += 1
            elif diff == 0:
                continue
            else:
                ans = max(ans, count)
                count = 1
        return max(ans, count)