class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        ans = 0
        min_i = max_i = bad_i = -1
        for i in range(len(nums)):
            if nums[i] < minK or nums[i] > maxK:
                bad_i = i
            
            if nums[i] == minK:
                min_i = i
                
            if nums[i] == maxK:
                max_i = i
            
            if min_i > bad_i and max_i > bad_i:
                ans += min(min_i, max_i) - bad_i
        return ans