class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        @cache
        def helper(remaining: int) -> int:
            if remaining == 0:
                return 1
            
            if remaining < 0:
                return 0
            
            combs = 0
            for num in nums:
                combs += helper(remaining - num)
            
            return combs
        
        n = len(nums)
        return helper(target)