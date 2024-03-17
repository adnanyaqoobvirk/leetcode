class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = []
        for i in range(n):
            ans.append(0)
            nums[i] = nums[i]**2
        
        p = n - 1
        l = 0
        r = n - 1
        while l <= r:
            if nums[l] >= nums[r]:
                ans[p] = nums[l]
                l += 1
            else:
                ans[p] = nums[r]
                r -= 1
            p -= 1
        
        return ans