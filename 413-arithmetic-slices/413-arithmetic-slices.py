class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums)
        
        ans = 0
        for i in range(n - 2):
            diff = nums[i + 1] - nums[i]
            for j in range(i + 2, n):
                if diff != nums[j] - nums[j - 1]:
                    break
                ans += 1
        return ans
                