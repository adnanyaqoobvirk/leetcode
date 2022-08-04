class Solution:
    def smallestRangeII(self, nums: List[int], k: int) -> int:
        nums.sort()
        
        max_val, min_val = nums[-1], nums[0]
        ans = max_val - min_val
        for i in range(len(nums) - 1):
            ans = min(
                ans, 
                max(max_val - k, nums[i] + k) - min(min_val + k, nums[i + 1] - k)
            )
        return ans