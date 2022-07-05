class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        @cache
        def helper(remaining: int) -> int:
            if remaining < 0:
                return 0
            
            if remaining == 0:
                return 1
            
            ans = 0
            for num in nums:
                ans += helper(remaining - num)
                
            return ans
        return helper(target)