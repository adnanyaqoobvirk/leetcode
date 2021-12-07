class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        cnums = sorted(nums)
        
        lo, hi = 0, len(nums) - 1
        i = 0
        while lo < hi:
            nums[i], nums[i + 1] = cnums[lo], cnums[hi]
            lo += 1
            hi -= 1
            i += 2
        
        if lo == hi:
            nums[-1] = cnums[lo]