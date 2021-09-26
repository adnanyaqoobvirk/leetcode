class Solution:
    def validSubarrays(self, nums: List[int]) -> int:
        ans = 0
        for i in range(len(nums)):
            left = nums[i]
            for j in range(i, len(nums)):
                if left <= nums[j]:
                    ans += 1
                else:
                    break
        return ans