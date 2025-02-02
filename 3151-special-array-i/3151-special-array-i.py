class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        for i in range(1, len(nums)):
            if not ((nums[i - 1] ^ nums[i]) & 1):
                return False
        return True