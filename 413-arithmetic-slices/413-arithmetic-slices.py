class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums)
        
        ans = 0
        for i in range(n - 2):
            diff = nums[i + 2] - nums[i + 1]
            if diff != nums[i + 1] - nums[i]:
                continue
            ans += 1
            
            for j in range(i + 3, n):
                if diff != nums[j] - nums[j - 1]:
                    break
                ans += 1
        return ans
                