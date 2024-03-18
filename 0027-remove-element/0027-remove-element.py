class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        
        for f in range(len(nums)):
            if nums[f] == val:
                continue
            
            nums[k] = nums[f]
            k += 1
            
        return k