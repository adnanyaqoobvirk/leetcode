class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        ans = 0
        for i in range(2, len(nums)):
            for j in range(i, len(nums)):
                if nums[j] - nums[j - 1] != nums[j - 1] - nums[j - 2]:
                    break
                ans += 1
        return ans