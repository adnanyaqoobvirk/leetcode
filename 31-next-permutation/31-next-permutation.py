class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def reverse(left: int, right: int) -> None:
            while left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
                
        n = len(nums)       
        for i in reversed(range(1, n)):
            if nums[i] > nums[i - 1]:
                j = i
                while j < n and nums[j] > nums[i - 1]:
                    j += 1
                nums[i - 1], nums[j - 1] = nums[j - 1], nums[i - 1]
                reverse(i, n - 1)
                break
        else:
            reverse(0, n - 1)