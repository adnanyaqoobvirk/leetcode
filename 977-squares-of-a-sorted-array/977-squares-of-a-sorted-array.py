class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        for i in range(n):
            if nums[i] >= 0:
                break
        
        ans, lo, hi = [], i - 1, i
        while lo >= 0 and hi < n:
            if abs(nums[lo]) > abs(nums[hi]):
                ans.append(nums[hi] ** 2)
                hi += 1
            else:
                ans.append(nums[lo] ** 2)
                lo -= 1
        
        for j in reversed(range(lo + 1)):
            ans.append(nums[j] ** 2)
        
        for j in range(hi, n):
            ans.append(nums[j] ** 2)
            
        return ans