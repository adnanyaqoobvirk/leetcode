class Solution:
    def jump(self, nums: List[int]) -> int:
        @cache
        def helper(i: int) -> int:
            if i > n:
                return float('inf')
            
            if i == n:
                return 0
            
            ans = float('inf')
            for j in range(1, min(n + 1, nums[i] + 1)):
                ans = min(ans, 1 + helper(i + j))
            
            return ans
        
        n = len(nums) - 1
        return helper(0)