class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        n = len(nums)

        for i in reversed(range(1, n)):
            p = i - 1
            if nums[i] > nums[p]:
                j = i
                while j < n and nums[j] > nums[p]:
                    j += 1
                nums[p], nums[j - 1] = nums[j - 1], nums[p]

                j = n - 1
                while i < j:
                    nums[i], nums[j] = nums[j], nums[i]
                    i += 1
                    j -= 1
                break
        else:
            nums.reverse()
                