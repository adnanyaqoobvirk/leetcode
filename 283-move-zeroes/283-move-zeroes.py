class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = None
        for j in range(len(nums)):
            if i is None:
                if nums[j] == 0:
                    i = j
            elif nums[j] != 0:
                nums[i], nums[j] = nums[j], 0
                i += 1