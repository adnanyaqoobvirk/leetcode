class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        back = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[back] = nums[i]
                back += 1
        return back