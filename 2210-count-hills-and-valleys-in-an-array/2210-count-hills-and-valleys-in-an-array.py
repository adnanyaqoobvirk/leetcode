class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        ans = 0
        l = 0
        for r in range(2, len(nums)):
            if nums[r - 1] == nums[r]:
                continue
            
            if nums[l] < nums[r - 1] > nums[r]:
                ans += 1
            elif nums[l] > nums[r - 1] < nums[r]:
                ans += 1
                
            l = r - 1
        return ans
        