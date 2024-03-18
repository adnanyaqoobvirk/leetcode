class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n = len(nums)
        k = 0
        
        for f in range(n):
            if nums[f] == val:
                continue
            
            nums[k] = nums[f]
            k += 1
            
        return k