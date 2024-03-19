class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 1
        
        for f in range(1, len(nums)):
            if nums[f] == nums[k - 1]:
                continue
            
            nums[k] = nums[f]
            k += 1
            
        return k