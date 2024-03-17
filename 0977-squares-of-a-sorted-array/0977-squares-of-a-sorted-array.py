class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0] * n
        
        p = n - 1
        l = 0
        r = n - 1
        while l <= r:
            if nums[l]**2 >= nums[r]**2:
                ans[p] = nums[l]**2
                l += 1
            else:
                ans[p] = nums[r]**2
                r -= 1
            p -= 1
        
        return ans