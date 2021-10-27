class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        reds = whites = blues = 0
        
        for num in nums:
            if num == 0:
                reds += 1
            elif num == 1:
                whites += 1
            else:
                blues += 1
        
        for i in range(reds):
            nums[i] = 0

        for j in range(reds, reds + whites):
            nums[j] = 1

        for k in range(reds + whites, reds + whites + blues):
            nums[k] = 2