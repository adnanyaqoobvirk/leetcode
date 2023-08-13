class Solution:
    def validPartition(self, nums: List[int]) -> bool:
        @cache
        def helper(pos: int) -> bool:
            if pos == n:
                return True
            elif pos > n:
                return False
            
            ans = False
            if pos + 1 < n and nums[pos] == nums[pos + 1]:
                ans = ans or helper(pos + 2)
            
            if pos + 2 < n:
                if nums[pos] == nums[pos + 1] == nums[pos + 2]:
                    ans = ans or helper(pos + 3)
                elif nums[pos] == nums[pos + 1] - 1 == nums[pos + 2] - 2:
                    ans = ans or helper(pos + 3)
            return ans
        
        n = len(nums)
        return helper(0)