class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        pp = nums[0] & 1
        for i in range(1, len(nums)):
            cp = nums[i] & 1
            if pp == cp:
                return False
            pp = cp
        return True